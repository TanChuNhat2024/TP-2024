import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.google.gson.Gson; // Assuming you use Gson for JSON processing

public class PhoneClient {

    private static final String BASE_URL = "http://127.0.0.1:5000"; // Replace with your server URL
    private static final Gson gson = new Gson();

    public static List<Map<String, Object>> getPhones() throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/phones"))
                .GET()
                .build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        return gson.fromJson(response.body(), List.class);
    }

    public static Map<String, Object> getPhoneById(String phoneId) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/phones/" + phoneId))
                .GET()
                .build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        return gson.fromJson(response.body(), Map.class);
    }

    public static Map<String, Object> addPhone(Map<String, Object> phone) throws IOException, InterruptedException {
        String jsonPhone = gson.toJson(phone);
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/phones"))
                .POST(HttpRequest.BodyPublishers.ofString(jsonPhone))
                .headers("Content-Type", "application/json")
                .build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        return gson.fromJson(response.body(), Map.class);
    }

    public static Map<String, Object> updatePhone(String phoneId, Map<String, Object> phone) throws IOException, InterruptedException {
        String jsonPhone = gson.toJson(phone);
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/phones/" + phoneId))
                .PUT(HttpRequest.BodyPublishers.ofString(jsonPhone))
                .headers("Content-Type", "application/json")
                .build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        return gson.fromJson(response.body(), Map.class);
    }

    public static boolean deletePhone(String phoneId) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/phones/" + phoneId))
                .DELETE()
                .build();
        HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        return true; // Assuming successful deletion returns no content
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        // Usage example
        List<Map<String, Object>> inventory = getPhones();
        System.out.println("Inventory: " + inventory);

        Map<String, Object> newPhone = new HashMap<>();
        newPhone.put("phone_id", "123");
        newPhone.put("model", "iPhone 12");
        newPhone.put("quantity", 10);

        Map<String, Object> addedPhone = addPhone(newPhone);
        System.out.println("Added Phone: " + addedPhone);

        Map<String, Object> phoneToUpdate = new HashMap<>();
        phoneToUpdate.put("quantity", 12);

        Map<String, Object> updatedPhone = updatePhone(addedPhone.get("phone_id").toString(), phoneToUpdate);
        System.out.println("Updated Phone: " + updatedPhone);

        boolean deletedPhone = deletePhone(updatedPhone.get("phone_id").toString());
        System.out.println("Phone Deleted: " + deletedPhone);
    }
}
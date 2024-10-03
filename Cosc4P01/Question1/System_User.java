import java.util.HashMap;
import java.util.Map;

public class System_User {
    private Map<String, String> users = new HashMap<>();
    private Map<String, Integer> failedAttempts = new HashMap<>();
    private static final int MAX_ATTEMPTS = 3;

    public void registerUser(String username, String password) {
        users.put(username, password);
        failedAttempts.put(username, 0);
    }

    public String login(String username, String password) {
        if (username == null || username.isEmpty() || password == null || password.isEmpty()) {
            return "Username/Password cannot be empty";
        }

        if (!users.containsKey(username)) {
            return "Invalid Credentials";
        }

        if (failedAttempts.get(username) >= MAX_ATTEMPTS) {
            return "Account locked due to too many failed login attempts";
        }

        if (users.get(username).equals(password)) {
            failedAttempts.put(username, 0); // Reset attempts on successful login
            return "Successful Login, Redirecting to Dashboard";
        } else {
            failedAttempts.put(username, failedAttempts.get(username) + 1);
            return "Invalid Credentials";
        }

    }
}

import java.util.HashMap;
import java.util.Map;

public class System_User_Refactored {
    private Map<String, String> users = new HashMap<>();
    private Map<String, Integer> failedAttempts = new HashMap<>();
    private static final int MAX_ATTEMPTS = 3;

    public void registerUser(String username, String password) {
        users.put(username, password);
        failedAttempts.put(username, 0);
    }

    public String login(String username, String password) {
        if (isEmpty(username) || isEmpty(password)) {
            return "Username/Password cannot be empty";
        }

        if (!isUserRegistered(username)) {
            return "Invalid Credentials";
        }

        if (isAccountLocked(username)) {
            return "Account locked due to too many failed login attempts";
        }

        if (isPasswordCorrect(username, password)) {
            resetFailedAttempts(username);
            return "Successful Login, Redirecting to Dashboard";
        } else {
            increaseFailedAttempts(username);
            return "Invalid Credentials";
        }
    }

    private boolean isEmpty(String str) {
        return str == null || str.isEmpty();
    }

    private boolean isUserRegistered(String username) {
        return users.containsKey(username);
    }

    private boolean isAccountLocked(String username) {
        return failedAttempts.get(username) >= MAX_ATTEMPTS;
    }

    private boolean isPasswordCorrect(String username, String password) {
        return users.get(username).equals(password);
    }

    private void resetFailedAttempts(String username) {
        failedAttempts.put(username, 0);
    }

    private void increaseFailedAttempts(String username) {
        failedAttempts.put(username, failedAttempts.get(username) + 1);
    }
}


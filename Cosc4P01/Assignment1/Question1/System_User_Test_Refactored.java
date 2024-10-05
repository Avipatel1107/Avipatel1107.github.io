import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class System_User_Test_Refactored {
    private System_User_Refactored loginSystem;

    @BeforeEach
    public void setUp() {
        loginSystem = new System_User_Refactored();
    }

    @Test
    public void successRegistrationTest() {
        loginSystem.registerUser("Avi", "Avi@2024");
        assertLoginSuccess("Avi", "Avi@2024");
    }

    @Test
    public void successLoginTest() {
        loginSystem.registerUser("Pal", "Pal#Secure123");
        assertLoginSuccess("Pal", "Pal#Secure123");
    }

    @Test
    public void passwordIncorrectTest() {
        loginSystem.registerUser("Shailey", "Shailey$Pass456");
        assertEquals("Invalid Credentials", loginSystem.login("Shailey", "Some@password"));
    }

    @Test
    public void threeFailAttemptLockoutTest() {
        loginSystem.registerUser("Avi", "Avi@Password789");

        for (int i = 0; i < 3; i++) {
            assertEquals("Invalid Credentials", loginSystem.login("Avi", "MCFC>MUFC"));
        }
        assertEquals("Account locked due to too many failed login attempts", loginSystem.login("Avi", "Avi@Password789"));
    }

    @Test
    public void usernameOrPasswordEmptyTest() {
        assertEquals("Username/Password cannot be empty", loginSystem.login("", "somepassword"));
        assertEquals("Username/Password cannot be empty", loginSystem.login("someuser", ""));
    }

    // Helper method to assert successful login
    private void assertLoginSuccess(String username, String password) {
        assertEquals("Successful Login, Redirecting to Dashboard", loginSystem.login(username, password));
    }
}

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class System_User_Test {
    private System_User userLogin;

    @BeforeEach
    public void setUp() {
        userLogin = new System_User();
    }
    @Test
    public void successRegistrationTest() {
        userLogin.registerUser("Avi", "Avi@2024");
        String result = userLogin.login("Avi", "Avi@2024");
        assertEquals("Successful Login, Redirecting to Dashboard", result);
    }
    @Test
    public void successLoginTest() {
        userLogin.registerUser("Pal", "Pal#Secure123");
        String result = userLogin.login("Pal", "Pal#Secure123");
        assertEquals("Successful Login, Redirecting to Dashboard", result);
    }
    @Test
    public void passwordIncorrectTest() {
        userLogin.registerUser("Shailey", "Shailey$Pass456");
        String result = userLogin.login("Shailey", "wrongpassword");
        assertEquals("Invalid Credentials", result);
    }
    @Test
    public void threeFailAttemptLockoutTest() {
        userLogin.registerUser("Avi", "Avi@Password789");
        String firstAttempt = userLogin.login("Avi", "MCFC>MUFC");
        assertEquals("Invalid Credentials", firstAttempt);
        String secondAttempt = userLogin.login("Avi", "MCFC>MUFC");
        assertEquals("Invalid Credentials", secondAttempt);
        String thirdAttempt = userLogin.login("Avi", "MCFC>MUFC");
        assertEquals("Invalid Credentials", thirdAttempt);
        String fourthAttempt = userLogin.login("Avi","MCFC>MUFC");
        assertEquals("Account locked due to too many failed login attempts", fourthAttempt);
        String subsequentAttempt = userLogin.login("Avi", "Avi@Password789");
        assertEquals("Account locked due to too many failed login attempts", subsequentAttempt);
    }
    @Test
    public void usernameOrPasswordEmptyTest() {
        String result = userLogin.login("", "somepassword");
        assertEquals("Username/Password cannot be empty", result);
        result = userLogin.login("someuser", "");
        assertEquals("Username/Password cannot be empty", result);
    }
}

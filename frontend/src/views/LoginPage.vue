<template>

  <div class="login-page">
    <h1>Sign In</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">Club username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Sign In</button>
      <div>
        <p><a href="mailto:esd.uoa@gmail.com">New Club?</a></p>
      </div>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>

</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();

const username = ref("");
const password = ref("");
const errorMessage = ref("");

const handleLogin = async () => {
  if (!username.value || !password.value) {
    errorMessage.value = "Please enter both your club's username and password. Click on the 'New Club?' link if you're having trouble signing in.";
    return;
  }

  // Clear any previous error message
  errorMessage.value = "";

  try {
    // const response = await axios.post("http://localhost:8000/api/token/", { // absolute URL, assuming the server is running on localhost:8000
    const response = await axios.post("/api/token/", { // relative URL, assuming the server is running on the same host
      username: username.value,
      password: password.value,
    }, {
      headers: {
        "Content-Type": "application/json",
      },
    });

    const token = response.data; // All token data (not just access token)
    if (token) {
      localStorage.setItem("jwt", token);

      // For debugging:
      alert("Logged in successfully!");
      console.log("Server response:", response.data);

      // FINAL TODO: Redirect to display items page
      // Current TODO: Redirect to add new items page using Vue
      router.push({ name: "AddNewItem" });

    } else {
      alert("Login failed: No token received.");
      console.log("Login failed: No token received.");
      errorMessage.value = "Login failed: No token received.";
    }
  } catch (error) {
    errorMessage.value = "Login failed: Invalid username or password.";
  }
};
</script>


<style scoped>
* {
  font-family: 'Inter', sans-serif;
  /* Apply Inter font globally */
  border-radius: 20px;
}

.login-page {
  min-width: 200px;
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ccc;
  background-color: #FFFFFF;
}

h1 {
  text-align: center;
}

label {
  display: block;
  margin-bottom: 5px;
  font-size: smaller;
}

input {
  width: 95%;
  padding: 8px;
  font-size: medium;
  margin-bottom: 20px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #1B0303;
  color: white;
  font-size: 16px;
  font-weight: bold;
  border: none;
  margin-top: 20px;
}

button:hover {
  background-color: #1B0303;
}
</style>
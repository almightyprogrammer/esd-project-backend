<template>
    
    <div class="login-page">
        <h1>Sign In</h1>
        <!-- <form @submit.prevent="handleLogin"> -->
        <form>
            <div>
                <label for="username">Club username:</label>
                <!-- <input type="text" id="username" v-model="username" required /> -->
                <input type="text" id="username" required />
            </div>
            <div>
                <label for="password">Password:</label>
                <!-- <input type="password" id="password" v-model="password" required /> -->
                <input type="password" id="password" required />
            </div>
            <button type="submit">Sign In</button>
            <!-- New club -->
            <div>
                <p><a href="mailto:esd.uoa@gmail.com">New Club?</a></p>
            </div>
        </form>
        <!-- <p v-if="errorMessage" class="error">{{ errorMessage }}</p> -->
    </div>
    
</template>

<script>
export default {
    name: 'LoginPage',
    data() {
        return {
            username: '',
            password: '',
            errorMessage: ''
        };
    },
    methods: {
        handleLogin() {
            // Implement login logic here
            // For example, send a request to the backend API
            console.log('Logging in with', this.username, this.password);
        }
    }
};
</script>

<!-- Style -->
<style scoped>
    * {
        font-family: 'Inter', sans-serif; /* Apply Inter font globally */
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
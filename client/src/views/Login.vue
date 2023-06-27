<template>
  <div class="login">
    <h1>Login Page</h1>
    <form @submit.prevent="login">
      <label for="username">Username</label>
      <input type="text" id="username" v-model="username" />
      <label for="password">Password</label>
      <!-- <input type="password" id="password" v-model="password" /> -->
      <el-input v-model="password" type="password" placeholder="Please input password" show-password />
      <button type="submit">Login</button>
    </form>
  </div>
  <div class="flex items-center justify-center">
    <el-button type="danger" >Sign Up</el-button>
  </div>
  
</template>
  
<script setup>
import { ref } from 'vue';

const username = ref('');
const password = ref('');

const login = () => {
  // Perform login logic here
  // For example, make an API request with the entered username and password
  // Upon successful login, navigate to the desired route
  if (username.value === 'admin' && password.value === 'password') {
    //   $router.push('/dashboard');
  } else {
    alert('Invalid username or password');
  }
};
</script>
  
<style scoped>
.login {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

h1 {
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

label {
  font-weight: bold;
}

input[type='text'],
input[type='password'] {
  padding: 6px 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 8px 12px;
  background-color: #4285f4;  /* 会影响到el-button */
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
  
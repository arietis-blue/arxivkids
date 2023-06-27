<template>
  <div class="login-container">
    <h2 class="login-title"></h2>
    <form @submit.prevent="login">
      <div class="input-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" placeholder="Enter your username" required>
      </div>
      <div class="input-group">
        <label for="password">Password:</label>
        <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password" placeholder="Enter your password" required>
        <input type="checkbox" v-model="showPassword"> Show Password
      </div>
      <div class="button-group">
        <button type="submit" class="signin-button">Sign In</button>
        <button type="button" class="register-button" @click="register">Register</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      showPassword: false
    };
  },
  methods: {
    login() {
      // 处理登录逻辑
      console.log('Username:', this.username);
      console.log('Password:', this.password);
      // 发送登录请求或执行其他操作
    },
    register() {
      // 处理注册逻辑
      console.log('Registering...');
      // 执行注册操作
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

form {
  width: 400px;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 20px;
}

.login-title {
  text-align: center;
}

.input-group {
  margin-bottom: 10px;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.button-group {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

button {
  width: 48%;
  padding: 10px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.signin-button {
  background-color: #4CAF50;
}

.register-button {
  background-color: #4285F4;
}
</style>

<template>
  <router-view />

  <AuthOverlay v-if="isLoginOpen" />
</template>

<!-- <script>
export default {
    name: 'App'
}
</script> -->

<script setup>
import { ref } from "vue";

const isLoginOpen = ref(false)
</script>

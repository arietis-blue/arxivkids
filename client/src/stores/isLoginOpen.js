import { defineStore } from 'pinia'
import { ref } from "vue"

export const useIsLoginOpenStore = defineStore('is-login-open', () => {
    const isLoginOpen = ref(false)
    return { isLoginOpen }
})
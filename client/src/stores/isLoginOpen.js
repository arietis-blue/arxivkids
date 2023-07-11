import { defineStore } from 'pinia'
import { ref } from "vue"

export const useIsLoginOpenStore = defineStore('isLoginOpen', () => {
    const isLoginOpen = ref(false)
    return { isLoginOpen }
})
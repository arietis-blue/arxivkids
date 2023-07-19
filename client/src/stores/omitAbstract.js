import { defineStore } from 'pinia'
import { ref } from "vue"

export const useOmitAbstractStore = defineStore('omit-abstract', () => {
    const omitAbstract = ref(true)
    return { omitAbstract }
})
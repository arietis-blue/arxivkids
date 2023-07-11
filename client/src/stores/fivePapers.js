import { defineStore } from 'pinia'
import { ref } from "vue"

export const useFivePapersStore = defineStore('fivePapers', () => {
    // const fivePapers = ref([])
    const fivePapers = ref()
    return { fivePapers }
})
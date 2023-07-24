import { defineStore } from 'pinia'
import { ref } from "vue"

export const useFivePapersStore = defineStore('five-papers', () => {
    // const fivePapers = ref([])   //() or ([])都行貌似
    const fivePapers = ref("")
    return { fivePapers }
})
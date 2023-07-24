import { defineStore } from 'pinia'
import { ref } from "vue"

export const useFivePapersStore = defineStore('five-papers', () => {
    // const fivePapers = ref()   //() 是不行的，会有画面が真っ白になるバグ 血痛的教训；但意外""似乎work
    const fivePapers = ref([])
    return { fivePapers }
})
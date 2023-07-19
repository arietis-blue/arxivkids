import { defineStore } from 'pinia'
import { ref } from "vue"

export const useCurrentDetailPaperStore = defineStore('current-detail-paper', () => {
    const currentDetailPaper = ref()
    return { currentDetailPaper }
})
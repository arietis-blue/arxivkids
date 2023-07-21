import { defineStore } from 'pinia'
import { ref } from "vue"

export const useWaitingStore = defineStore('waiting', () => {
    let waitingArxiv = ref(false)
    let waitingPaper = ref(false)

    return { waitingArxiv, waitingPaper }
})
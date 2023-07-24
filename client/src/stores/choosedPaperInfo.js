import { defineStore } from 'pinia'
import { ref } from "vue"

export const useChoosedPaperInfoStore = defineStore('choosed-paper-info', () => {
    const Title_En = ref("")
    const Title_Ja = ref("")
    const Published = ref("")
    const Pdf_url = ref("")
    const Authors = ref([])
    const Categories = ref([])
    const Paper_ID = ref("")
    const Content_En = ref("")

    return { Title_En, Title_Ja, Authors, Categories, Published, Pdf_url, Paper_ID, Content_En }
})
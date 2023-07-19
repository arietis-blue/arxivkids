import { defineStore } from 'pinia'
import { ref } from "vue"

export const useHasSearchedStore = defineStore('has-searched', () => {
    const hasSearched = ref(false)
    // 花括号波括弧绝对不能省略
    return { hasSearched }
})
<template>
    <div >
        <a :href="paper.Pdf_url">pdf</a>
    </div>
</template>

<script setup>
import { defineProps, toRefs, ref } from "vue"
// import { useFivePapersStore } from '../stores/fivePapers'
// const fivePapersStore = useFivePapersStore()
const props = defineProps({
    Title_En: String,
    Title_Ja: String,

})


</script>
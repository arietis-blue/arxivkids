<template>
    <div id="AuthOverlay"
        class="fixed flex items-center justify-center z-50 top-0 left-0 w-full h-full bg-black bg-opacity-50">

        <div class="relative bg-white w-full max-w-[470px] h-[70%] p-4 rounded-lg">

            <div class="w-full flex justify-end">
                <button @click="isLoginOpenStore.isLoginOpen = false" class="p-1.5 rounded-full w-8 h-8 bg-gray-100 hover:bg-gray-300">
                    <!-- 完全不圆，用了rounded-fullけど，要加w,h才圆 -->
                    <el-icon :size="20">
                        <CloseBold />
                    </el-icon>
                </button>
            </div>

            <Login v-if="isRegister" />


            <div class="absolute flex items-center justify-center py-5 left-0 bottom-0 border-t w-full">
                <span v-if="isRegister" class="text-[14px] text-gray-600">Don’t have an account?</span>
                <span v-else class="text-[14px] text-gray-600">Already have an account?</span>
                <button 
                    @click="isRegister = !isRegister" 
                    class="text-[14px] text-[#F02C56] font-semibold pl-1"
                >
                    <span v-if="isRegister">Sign up</span>
                    <span v-else>Log in</span>
                </button>
            </div>

        </div>

    </div>
</template>

<script setup>
import { ref } from "vue";
import { CloseBold } from "@element-plus/icons-vue"
import Login from "./Login.vue"

import { useIsLoginOpenStore } from '../stores/isLoginOpen'
const isLoginOpenStore = useIsLoginOpenStore()

let isRegister = ref(true)


</script>

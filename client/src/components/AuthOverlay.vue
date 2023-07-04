<template>
    <div id="AuthOverlay"
        class="fixed flex items-center justify-center z-50 top-0 left-0 w-full h-full bg-black bg-opacity-50">

        <div class="relative bg-white w-full max-w-[470px] h-[70%] p-4 rounded-lg">

            <div class="w-full flex justify-end">
                <button @click="isLoginOpen = false" class="p-1.5 rounded-full bg-gray-100">
                    <!-- 完全不圆，用了rounded-fullけど -->
                    <el-icon :size="20">
                        <CloseBold />
                    </el-icon>
                </button>
                <el-button :icon="CloseBold" circle />
            </div>


            <div class="absolute flex items-center justify-center py-5 left-0 bottom-0 border-t w-full">
                <span class="text-[14px] text-gray-600">Don’t have an account?</span>
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
let isRegister = ref(true)

const divRef = ref(null);
let isDragging = false;
let offset = { x: 0, y: 0 };

const startDrag = (e) => {
  isDragging = true;
  offset.x = e.offsetX;
  offset.y = e.offsetY;
};

const drag = (e) => {
  if (isDragging) {
    const x = e.clientX - offset.x;
    const y = e.clientY - offset.y;
    divRef.value.style.left = x + 'px';
    divRef.value.style.top = y + 'px';
  }
};

const stopDrag = () => {
  isDragging = false;
};

</script>
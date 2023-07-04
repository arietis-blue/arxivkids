<template>
    <!-- <div>aaa</div> -->
    <div id="PaperRow">
        <div 
            class="
                flex items-center justify-between
                border-b 
                mb-2
                bg-orange-200
                rounded-3xl
                max-w-[780px]
                hover:border-red-200 
                hover:border-t 
                hover:border-y-2 
                hover:border-x
                cursor-pointer
            "
            
        >
            <div class="flex items-center px-4 py-2">

                <div class="flex items-center w-full">
                    <!-- 定义路由转移 -->
                    <router-link :to="`/detailpaper/${id}`" class="w-full">

                        <div class="flex justify-between items-center">
                            <div class="flex items-center w-full">
                                <div class="font-semibold text-sm ml-4 truncate-from">
                                    title
                                </div>

                                <div class="flex items-center justify-between">
                                    <div class="mr-1.5 text-sm font-semibold truncate-subject">
                                        author
                                    </div>
                                    
                                    
                                </div>
                            </div>

                            <div class="text-sm text-gray-500 truncate-body pr-2">
                                       body
                                    </div>

                            
                        </div>
                    </router-link>
                </div>
                <router-link to="login" class="w-full">
                    <el-button type="warning" :icon="Star" circle />
                </router-link>
                
            </div>
        </div>
    </div>
</template>


<script setup>
import { Star } from "@element-plus/icons-vue"
</script>
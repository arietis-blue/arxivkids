<template>
    <!-- <div>aaa</div> -->
    <!--    <div id="PaperRow">-->
    <!--        <div -->
    <!--            class="-->
    <!--                flex items-center justify-between-->
    <!--                border-b -->
    <!--                mb-2-->
    <!--                bg-orange-200-->
    <!--                rounded-3xl-->
    <!--                max-w-[780px]-->
    <!--                hover:border-red-200 -->
    <!--                hover:border-t -->
    <!--                hover:border-y-2 -->
    <!--                hover:border-x-->
    <!--                cursor-pointer-->
    <!--            "-->
    <!--            -->
    <!--        >-->
    <!--            <div class="flex items-center px-4 py-2">-->

    <!--                <div class="flex items-center w-full">-->
    <!--                    &lt;!&ndash; 定义路由转移 &ndash;&gt;-->
    <!--                    <router-link :to="`/detailpaper/${id}`" class="w-full">-->

    <!--                        <div class="flex justify-between items-center">-->
    <!--                            <div class="flex items-center w-full">-->
    <!--                                <div class="font-semibold text-sm ml-4 truncate-from">-->
    <!--                                    title-->
    <!--                                </div>-->

    <!--                                <div class="flex items-center justify-between">-->
    <!--                                    <div class="mr-1.5 text-sm font-semibold truncate-subject">-->
    <!--                                        author-->
    <!--                                    </div>-->
    <!--                                    -->
    <!--                                    -->
    <!--                                </div>-->
    <!--                            </div>-->

    <!--                            <div class="text-sm text-gray-500 truncate-body pr-2">-->
    <!--                                       body-->
    <!--                                    </div>-->

    <!--                            -->
    <!--                        </div>-->
    <!--                    </router-link>-->
    <!--                </div>-->
    <!--                <router-link to="login" class="w-full">-->
    <!--                    <el-button type="warning" :icon="Star" circle />-->
    <!--                </router-link>-->
    <!--                -->
    <!--            </div>-->
    <!--        </div>-->
    <!--    </div>-->


    <div class="flex justify-center mb-4">
        <!-- <router-link :to="`/detailpaper/${id}`" class="w-7/10"> -->
        <router-link to="/detailpaper" class="w-7/10">
            <div class="bg-blue-100 rounded p-4 shadow-md">
                <div class="truncate">
                    <!-- <span class="font-bold text-lg">A Very Long English Title That Will Be Truncated If It Exceeds the
                        Maximum Lengthaaaaaaaaaaaaaaaaaaa</span> -->
                    <span class="font-bold text-lg">{{ titleEn }}</span>
                </div>
            </div>
            <div class="bg-blue-100 rounded p-4 shadow-md">
                <div class="truncate">
                    <!-- <span class="font-bold text-lg text-gray-500">超过指定长度时将被截断的很长的日语标题</span> -->
                    <span class="font-bold text-lg text-gray-500">{{ titleJp }}</span>
                </div>
            </div>
            <div class="bg-blue-100 rounded p-4 shadow-md">
                <div class="truncate">
                    <div>
                        <!-- <span class="text-base text-gray-500">John Doe</span> -->
                        <span class="text-base text-gray-500">{{ author }}</span>
                    </div>
                </div>
            </div>
        </router-link>
    </div>
</template>


<script setup>
import { Star } from "@element-plus/icons-vue"
import { defineProps, toRefs, ref } from "vue";

const props = defineProps({
    titleEn: String,
    titleJp: String,
    author: String,
})

const { id, text, date, backgroundColor } = toRefs(props);
</script>
<template>
    <TopNav />

    <div class="pt-[100px] 2xl:pl-[185px] lg:pl-[160px] lg:pr-0 pr-2 w-[calc(100%-90px)] max-w-[1800px] 2xl:mx-auto">
        <div class="flex w-[calc(100vw-230px)]">
            <img class="max-w-[100px] rounded-full" src="../assets/xjp.jpeg">

            <div class="ml-5 w-full">
                <div class="text-[30px] font-bold truncate">
                    User name
                    <!-- {{ $generalStore.allLowerCaseNoCaps($profileStore.name) }} -->
                </div>
                <div class="text-[18px] truncate">email</div>
                <button @click="$generalStore.isEditProfileOpen = true"
                    class="flex item-center rounded-md py-1.5 px-3.5 mt-3 text-[15px] font-semibold border hover:bg-gray-100">
                    <el-icon :size="20">
                        <Edit />
                    </el-icon>
                    <div class="ml-2">Edit profile</div>
                </button>
            </div>
        </div>

        <div class="flex items-center pt-4">
            <div class="mr-4">
                <span class="font-bold">20</span>
                <span class="text-gray-500 font-light text-[15px] pl-1.5">History</span>
            </div>
            <div>
                <span class="font-bold">10</span>
                <span class="text-gray-500 font-light text-[15px] pl-1.5">Liked</span>
            </div>
        </div>

        <div class="w-full flex items-center pt-4 border-b">
            <!-- 居中有问题啊 -->
            <div class="w-60 flex items-center text-center py-2 text-[17px] font-semibold border-b-2 border-b-black">
                <div><el-icon class="pt-3 mr-2 ">
                        <View />
                    </el-icon></div>
                    <el-badge :value="12" class="item">History</el-badge>
            </div>
            <div class="w-60 text-gray-500 text-center py-2 text-[17px] font-semibold">
                <el-icon>
                    <Star />
                </el-icon>
                <!-- Liked -->
                <el-badge :value="12" class="item">
                    <el-button>Liked</el-button>
                </el-badge>
            </div>
        </div>

        <!-- <PaperRow author="ABCDEF" /> -->

    </div>
</template>

<script setup>
// import PaperRow from "../components/PaperRow.vue";
</script>
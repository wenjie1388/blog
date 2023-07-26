<template>
  <el-container>
    <el-header style="width: 100%">
      <el-menu :default-active="appStore.menu" class="el-menu-demo" mode="horizontal" :ellipsis="false"
        @select="handleSelect">
        <div class="logo-box" style="display: flex; margin: auto 0">
          <h3>LOGO</h3>
          <!-- <el-image style="width: 100px; height: 58px;display: flex;"
            src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" fit="contain" /> -->
        </div>
        <el-menu-item index="/">首页</el-menu-item>
        <div class="flex-grow" style="display: flex">
          <!-- <el-input v-model.trim="search" size="large" @keyup.enter.native="toSearch()" placeholder="Please Input"
            :suffix-icon="Search" /> -->
        </div>
      </el-menu>
    </el-header>
    <el-main style="width: 100%; background: #fafafa; height: 100%; min-height: 1080px">
      <RouterView />
    </el-main>
    <div style="width: 100%; text-align: center">
      <router-link class="user-box" to="login">登录</router-link>
    </div>
  </el-container>
</template>
<script setup lang="ts">
// 系统依赖
import { ref, onMounted, onUpdated, reactive } from "vue";
import { Search } from "@element-plus/icons-vue";
import { RouterLink, RouterView } from "vue-router";

// 状态依赖
import { useAppStore } from "@/stores/modules/app";
const appStore = useAppStore();

// 路由管理依赖
import { useRoute } from "vue-router";
import router from "@/router";

// 搜索框
var search = ref("");
function toSearch() {
  if (search.value == "") {
    router.push("/");
  } else {
    router.push({
      path: "/search",
      query: {
        body: search.value,
      },
    });
  }
}

const handleSelect = (key: string, keyPath: string[]) => {
  appStore.menu = key;
  router.push(key);
};
</script>

<style scoped></style>

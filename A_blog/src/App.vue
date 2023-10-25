<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false"
          @select="handleSelect">
          <div class="logo-container">Wenjie's Blog</div>
          <!-- <el-menu-item index="0" class="no-hover">Wenjie's Blog</el-menu-item> -->
          <div class="flex-grow" />
          <el-menu-item index="1">首页</el-menu-item>
          <el-sub-menu index="2">
            <template #title>文章浏览</template>
            <el-menu-item index="2-1">文章分类</el-menu-item>
            <el-menu-item index="2-2">文章标签</el-menu-item>
            <el-menu-item index="2-3">文章推荐</el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-header>
      <el-main>
        <indexVue />
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>

<script setup lang="ts">
// 组件依赖
import indexVue from "@/views/index.vue";

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

const activeIndex = ref("1");
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

<style scoped>
.flex-grow {
  flex-grow: 1;
}

main {
  background: rgba(244, 245, 247, 1);
  padding: 0;
  margin: 0;
}

.el-header {
  padding: 0;
}
</style>

<template>
  <div>
    h
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>{{ article?.title }}</span>
          <router-link class="user-box" :to="{ path: '/article/', params: { article: article?.id } }">查看详情</router-link>
        </div>
      </template>
      <div key="" class="text item">{{ article?.body }}</div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { reactive, toRef } from "vue";
import { ArticleList } from "@/api/article/type";
const props = defineProps({
  article: Object,
  msg: String,
});

console.log("h", props.article);
</script>

<style lang="scss">
.el-card {
  .el-card__header {
    padding: calc(var(--el-card-padding) - 2px) var(--el-card-padding);
    border-bottom: 1px solid var(--el-card-border-color);
    box-sizing: border-box;
  }

  .el-card__body {}
}
</style>

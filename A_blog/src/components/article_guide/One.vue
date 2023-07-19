<template>
  <div>
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>{{ article?.title }}</span>
          <el-button class="button" text>查看详情</el-button>
        </div>
      </template>
      <div key="" class="text item">{{ article?.body }}</div>
    </el-card>
  </div>
</template>


<script setup lang="ts" >
import { reactive, toRef } from 'vue';
// import { ArticleList } from '@/api/article/type';
const props = defineProps({
  // article: Object,
  article: Object,
  msg: String,

})
</script>


<style lang="scss" >
.el-card {


  .el-card__header {
    padding: calc(var(--el-card-padding) - 2px) var(--el-card-padding);
    border-bottom: 1px solid var(--el-card-border-color);
    box-sizing: border-box;
  }

  .el-card__body {}

}
</style>

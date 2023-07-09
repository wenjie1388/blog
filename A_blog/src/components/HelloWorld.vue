<script setup lang="ts">
import { onMounted, reactive } from 'vue';
import { getUserInfo1Api } from "@/api/user/index";
import { UserInfo1 } from "@/api/user/type";

const userInfo1 = reactive({
  username: '',
  email: ''
})

async function init_user() {
  await getUserInfo1Api(3)
    .then((res) => {
      const data = res.data
      userInfo1.username = data.username;
      userInfo1.email = data.email;
    })
}

onMounted(() => {
  init_user();
});
const data = defineProps<{
  msg: string
}>()
// data.msg
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ userInfo1.username }}</h1>
    <h3>
      You’ve successfully created a project with
      <a href="https://vitejs.dev/" target="_blank" rel="noopener">Vite</a> +
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a>. What's next?
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {

  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router';
// import Card_one from '@/components/user/Card_one.vue';
import { getUserInfo1Api } from '@/api/user'

var user = ref({
  username: '',
  email: ''

})

async function initUser() {
  const params = {}
  getUserInfo1Api('v1', 4, params)
    .then((res) => {
      user = res.data
    })
}

onMounted(() => {
  initUser()
})

</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/微信头像.jpg" width="125" height="125" />

    <div class="wrapper">
      <span>{{ user.username }}</span>
      <span>{{ user.email }}</span>
      <nav>
        <RouterLink to="/">首页</RouterLink>
        <RouterLink to="/about">关于我</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>

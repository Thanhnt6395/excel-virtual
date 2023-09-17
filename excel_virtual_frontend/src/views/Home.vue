<template>
  <section id="home">
    <NavBar :user="getUser"></NavBar>
  </section>
</template>

<script setup>
import NavBar from '../components/NavBar.vue';
import { useRouter } from "vue-router";
import { computed, onMounted } from 'vue';
import { useStore } from 'vuex';

const router = useRouter()
const store = useStore()
const getUser = computed(() => store.state.user)

onMounted(async () => {
  await store.dispatch('user/getUser')
  if (!getUser) {
    router.push('/login')
  }
})
</script>

<style scoped>

</style>
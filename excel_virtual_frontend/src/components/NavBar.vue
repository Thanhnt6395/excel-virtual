<template>
  <section id="navbar">
    <div class="grid grid-cols-9 gap-1 bg-white px-5 py-2 relative h-16">
      <div class="col-span-5 sm:col-span-3 absolute translate-y-[-50%] top-[50%] left-[15px]">
        <div class="relative h-full">
          <font-awesome-icon
            icon="fa-solid fa-bars"
            size="lg"
            id="icon-menu"
            class="absolute translate-y-[-50%] top-[50%] left-0 text-gray-500 cursor-pointer hover:bg-gray-200 hover:rounded-[50%] p-2"
            @click="openMenu = !openMenu"
          />
          <font-awesome-icon
            icon="fa-solid fa-file-excel"
            size="2xl"
            class="absolute translate-y-[-50%] top-[50%] left-12 text-green-600"
          />
          <router-link
            to="/"
            class=" text-gray-500 text-xl absolute translate-y-[-50%] top-[50%] left-20 w-auto font-light"
            >Sheets</router-link
          >
        </div>
      </div>
      <div class="col-span-4 sm:col-span-3 grid grid-cols-3 gap-2 absolute translate-y-[-50%] top-[50%] right-[15px]">
        <div class="relative h-full col-span-2">
          <img
            :src="currentIcon"
            alt=""
            id="icon-lang"
            class="w-5 h-5 hover:cursor-pointer absolute translate-y-[-50%] top-[50%] right-0"
            @click="openLang = !openLang"
          />
          <div
            class="w-32 absolute translate-y-[50%] top-[10%] right-0 shadow-lg rounded-md border-gray-200 border-[1px]"
            id="modal-lang"
            v-if="openLang == true"
          >
            <ul>
              <li
                v-for="(lang, index) in langs"
                :key="index"
                class="flex text-gray-600 font-thin hover:bg-gray-100 hover:rounded p-2 hover:cursor-pointer"
                @click="changeLang(lang.key)"
              >
                <img :src="lang.icon" alt="" class="w-5 h-5 mr-2" />
                {{ lang.label }}
              </li>
            </ul>
          </div>
        </div>
        <div class="col-auto relative h-full hover:cursor-pointer">
          <font-awesome-icon icon="fa-solid fa-circle-user" size="2xl" v-if="!user || !user.avatar || user.avatar == ''" />
          <img :src="user.avatar" alt="" srcset="" v-else>
        </div>
      </div>
      <div class="col-span-9 sm:col-span-3 absolute translate-y-[50%] bottom-[-50%] left-[15px] right-[15px] sm:left-1/3 sm:right-1/3 sm:bottom-[50%]" id="search-bar">
        <div class="relative text-gray-400 focus-within:text-gray-600 h-full">
          <font-awesome-icon
            icon="fa-solid fa-magnifying-glass"
            class="text-gray-500 absolute w-6 h-6 translate-y-[-50%] top-[50%] left-3"
          />
          <input
            class="bg-gray-100 rounded-lg h-12 w-full pl-11 pr-3 focus:bg-white focus:border-gray-400 focus:shadow-md focus-visible:bg-white focus-visible:border-gray-400 focus-visible:shadow-md focus:outline-none"
            type="text"
            name=""
            id="search"
            :placeholder="homepage._search"
          />
        </div>
      </div>
    </div>

    <div
      class="h-full w-full sm:w-72 border-r-2 border-r-gray-200 shadow-lg absolute top-0 left-0 bg-white transition duration-300 ease-in"
      id="modal-menu"
      v-if="openMenu == true"
    >
      <div class="h-14 border-b-[1px] border-b-gray-200 relative">
        <h1
          class="text-gray-700 font-thin uppercase absolute translate-y-[-50%] top-[50%] text-center w-full text-xl"
        >
          Excel Virtual
        </h1>
      </div>

      <div class="border-b-[1px] border-b-gray-200 w-full grid grid-flow-row gap-1">
        <div class=" row-span-1 relative h-9">
          <font-awesome-icon icon="fa-solid fa-file-circle-plus" class=" text-gray-500 absolute translate-y-[-50%] top-[50%] left-[15px]" />
          <span class="text-gray-500 absolute translate-y-[-50%] top-[50%] left-[40px] font-thin">{{ homepage._new }}</span>
        </div>
        <div class=" row-span-1 relative h-9">
          <font-awesome-icon icon="fa-solid fa-box-archive" class=" text-gray-500 absolute translate-y-[-50%] top-[50%] left-[15px]" />
          <span class="text-gray-500 absolute translate-y-[-50%] top-[50%] left-[40px] font-thin">{{ homepage.myFile }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { mapState, useStore } from "vuex";

const openLang = ref(false);
const openMenu = ref(false);
const store = useStore()
const currentIcon = computed(() => store.getters["messages/currentIcon"])
const langs = store.getters["messages/langs"]
const homepage = computed(() => store.getters["messages/byPage"]('homepage'))
const props = defineProps({
  user: Object
})

function changeLang(lang) {
  store.dispatch('messages/setCurrentLang', lang)
  openLang.value = false;
}

onMounted(async () => {
  document.addEventListener("click", (e) => {
    if ((!e.target.id || e.target.id != "icon-lang") && openLang.value == true)
      openLang.value = false;
    if ((!e.target.id || e.target.id != "icon-menu") && openMenu.value == true)
      openMenu.value = false;
  });
  console.log({user: props.user})
});
</script>

<style scoped></style>

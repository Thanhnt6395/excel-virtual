<template>
  <section id="register">
    <div class="container mx-auto mt-[10rem]">
      <div class="box-content p-4 sm:p-8 shadow-md m-auto">
        <h1 class=" text-blue-950 font-bold uppercase mb-2 text-center text-3xl">Register</h1>
        <h3 class=" text-blue-950 font-light mb-7 text-center text-xl">Create your account</h3>
        <div class=" grid grid-cols-2 gap-x-3 gap-y-5">
          <div class=" col-span-2">
            <input type="text" name="" id="email" placeholder="Email" class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2">
          </div>
          <div class=" col-span-1">
            <input type="text" name="" id="first_name" placeholder="First Name" class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2">
          </div>
          <div class=" col-span-1">
            <input type="text" name="" id="last_name" placeholder="Last Name" class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2">
          </div>
          <div class=" col-span-2">
            <input type="text" name="" id="password" placeholder="Password" class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2">
          </div>
          <div class=" col-span-2">
            <input type="text" name="" id="repeat_password" placeholder="Repeat Password" class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2">
          </div>
          <div class=" col-span-1">
            <input type="checkbox" name="" id="show-password" class=" mr-3">
            <label for="show-password" class="text-blue-950 font-light">Show password</label>
          </div>
          <div class=" col-span-1 flex justify-end">
            <router-link to="/login" class="text-blue-950 font-light text-base hover:text-blue-600">Have an account ?</router-link>
          </div>
          <div class=" col-span-2 flex">
            <button type="button" class=" w-1/2 bg-blue-700 hover:bg-blue-500 text-white px-3 py-2 rounded uppercase mx-auto">Register</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>

</script>

<style scoped>

</style>
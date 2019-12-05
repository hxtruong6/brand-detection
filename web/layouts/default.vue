<template>
  <div id="app">
    <top-bar/>
    <nuxt/>
  </div>
</template>

<script>
import TopBar from "~/components/TopBar.vue";
export default {
  components: {
    TopBar
  }
};
</script>
 
<style>
#app {
  width: 100%;
  height: 100%; 
  min-height: 100vh;
  display: flex;
  flex-flow: column nowrap;
}
</style>

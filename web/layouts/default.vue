<template>
  <div id="app">
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span>Navigator Two</span>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <el-container>
        <top-bar />
        <el-main>
          <nuxt />
        </el-main>
      </el-container>
    </el-container>
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

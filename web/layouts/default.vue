<template>
  <el-container id="app" style="border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-menu :router="true" :default-active="currPath" ref="menu">
        <el-menu-item index="image" @click="onMenuItemClick">
          <i class="el-icon-picture-outline"></i>
          <span>Image</span>
        </el-menu-item>
        <el-menu-item index="video" @click="onMenuItemClick">
          <i class="el-icon-video-camera"></i>
          <span>Video</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header class="defaultHeader">
        <top-bar />
      </el-header>
      <el-main>
        <nuxt />
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import TopBar from "~/components/TopBar.vue";
import { mapState } from "vuex";

export default {
  components: {
    TopBar
  },
  computed: {
    ...mapState({
      isCollapse: state => state.sider.isSideBarOpen,
      currPath: state => state.sider.currPath
    })
  },
  methods: {
    onMenuItemClick(item) {
      this.$store.commit("sider/onSideBarClick", item.index);
    }
  }
};
</script>
 
<style lang='scss' scoped>
#app {
  width: 100%;
  height: 100%;
  min-height: 100vh;

  .defaultHeader {
    padding: 0;
    margin-bottom: 8px;
  }
}
</style>

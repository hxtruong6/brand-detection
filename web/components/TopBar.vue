<template>
  <div class="topBar">
    <img class="topBar__logo" src="~assets/images/butterfly-icon.png">
    <h1 class="topBar__header">{{header}}</h1>
  </div>
</template>

<script>
export default {
  name: "TopBar",
  data() {
    return {
      header: "Butterfly detector"
    };
  }
};
</script>

<style lang='scss' scoped>
.topBar {
  background-color: $primary-color-light;
  width: 100%;
  display: flex;
  padding: 4px;
  top: 0;

  &__logo {
    position: relative;
    left: 20px;
    padding: 3px;
    max-width: 50px;
    max-height: 50px;
    animation: moveInLeft 1s ease-in-out;
  }

  &__header {
    margin: auto;
    text-transform: uppercase;
    color: $white-color;
    font-size: 2rem;
  }
}
</style>

<template>
  <div class="imgDetector">
    <ImageUpload></ImageUpload>
    <ImageShow></ImageShow>
    <ImageInfo></ImageInfo>
  </div>
</template>

<script>
import ImageUpload from "~/components/ImageUpload.vue";
import ImageShow from "~/components/ImageShow.vue";
import ImageInfo from "~/components/ImageInfo.vue";

export default {
  name: "DetectorPage",
  components: {
    ImageUpload,
    ImageShow,
    ImageInfo
  }
};
</script>

<style>
.imgDetector {
  display: flex;
  flex: 1 1 0;
  flex-direction: row;
  justify-content: space-between;
  height: 100%;
  max-height: 92vh;
}
</style>

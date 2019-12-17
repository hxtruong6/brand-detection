<template>
  <div class="videoDetector">
    <VideoUpload></VideoUpload>
    <VideoShow></VideoShow>
    <VideoInfo></VideoInfo>
  </div>
</template>


<script>
import VideoUpload from "~/components/VideoUpload.vue";
import VideoShow from "~/components/VideoShow.vue";
import VideoInfo from "~/components/VideoInfo.vue";

export default {
  name: "DetectorPage",
  components: {
    VideoUpload,
    VideoShow,
    VideoInfo
  }
};
</script>

<style>
.detector {
  display: flex;
  flex: 1 1 0;
  flex-direction: row;
  justify-content: space-between;
}
</style>

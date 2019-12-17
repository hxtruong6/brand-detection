<script>
const currPath = localStorage.getItem("currPath") || "video";
export default {
  fetch({ redirect }) {
    redirect(`/${currPath}`);
  }
};
</script>

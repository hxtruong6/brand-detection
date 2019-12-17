export const state = () => ({
    isSideBarOpen: true,
    currPath: localStorage.getItem("currPath") || "video"
});

export const mutations = {
    toggleCollapse(state) {
        state.isSideBarOpen = !state.isSideBarOpen;
    },
    onSideBarClick(state, index) {
        state.currPath = index;
        localStorage.setItem("currPath", index);
    }
};

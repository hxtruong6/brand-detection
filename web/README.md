# Brand detection project

## 1. Web

Website is created for support user using. It allow for upload _image_ .or _video_ to detect their brand.

The result will show:

-   Image: the detected image of the origin uploaded image and recognized brands with logo, confidence, description,..
-   Video: the detected video (_in process (not completed)_) and recognized brands with _frequently_ appear percent and _cover_ percent in origin video.

### How to run

1. Install `npm` if not install yet

    `sudo apt-get install npm`

2. Install `yarn` if not install yet

    `sudo npm install -g yarn`

3. Install dependencies

    `yarn`

4. Run web

    `yarn dev`

=> Web will run at `http://localhost:3000/`. Open to using.

_Note_: you can skip step 1 and 2. Step 3 and 4 is required

### Result

-   Image UI
    ![Web UI](https://user-images.githubusercontent.com/24609363/71054523-e0d9ef00-2184-11ea-9cab-ad7a9122f751.png)

-   Video UI
    ![Video UI](https://user-images.githubusercontent.com/24609363/71054949-74f88600-2186-11ea-969b-e74a8d737594.png)

<details><summary>Click see result</summary>
<p>

### 1.Image

-   Test #1
    ![Test01](https://user-images.githubusercontent.com/24609363/71054522-e0415880-2184-11ea-9fdd-890affb02376.png)
    ![Test01 Result](https://user-images.githubusercontent.com/24609363/71054697-6e1d4380-2185-11ea-9854-b4511b60ef50.png)

-   Test #2
    ![Test02](https://user-images.githubusercontent.com/24609363/71054625-4332ef80-2185-11ea-97b0-3b3157c8f6c8.png)
    ![Test01 Result](https://user-images.githubusercontent.com/24609363/71054624-429a5900-2185-11ea-976e-0b9418bd7aa0.png)

### 2.Video

-   Video #
    ![Video](https://user-images.githubusercontent.com/24609363/71055102-fcde9000-2186-11ea-8153-5a089f158ac0.png)

    ![Video Res01](https://user-images.githubusercontent.com/24609363/71055202-52b33800-2187-11ea-88ac-65d12772f24f.png)
    ![Video Res02](https://user-images.githubusercontent.com/24609363/71055201-521aa180-2187-11ea-8f0e-7f87bb4ce2c8.png)

</p>
</details>

## 2. Server

## 3. Train model

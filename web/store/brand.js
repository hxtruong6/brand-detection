export const state = () => ({
    data: {
        coca: {
            description: `Coca-Cola (còn có tên gọi tắt là Coke) là một thương hiệu nước ngọt có ga chứa nước cacbon dioxit bão hòa được sản xuất bởi Công ty Coca-Cola. Coca-Cola ban đầu được điều chế bởi dược sĩ John Pemberton vào cuối thế kỷ XIX với mục đích trở thành một loại biệt dược. 
            Tuy nhiên, doanh nhân người Mỹ Asa Griggs Candler sau đó đã mua lại công thức loại thuốc uống này, và bằng những chiến thuật tiếp thị thông minh, ông đã đưa Coca-Cola trở thành một trong những sản phẩm dẫn đầu thị trường nước ngọt có ga trong thế kỷ XX. 
            Tên của Coca-Cola bắt nguồn từ hai thành phần nguyên bản của thức uống này: hạt cola (chứa nhiều caffein) và lá cây Coca. Hiện nay, công thức Coca-Cola vẫn còn là một ẩn số vềbí mật thương mại,dù có nhiều công thức thử nghiệm khác nhau đã được công bố rộng rãi.`,
            logo:
                "http://pngimg.com/uploads/cocacola_logo/cocacola_logo_PNG14.png"
        },
        aquafina: {
            description: `Aquana là nước tinh khiết. Nó bắt nguồn từ các nguồn nước công cộng và sau đó được
                tinh chế thông qua một quy trình khử khéo léo bảy bước gọi là Hydro-7 ™.
                Đây là một quy trình hiện đại bao gồm thẩm thấu ngược và các phương pháp lọc khác.
                Với công nghệ lọc Hydro-7 ™ độc quyền của PepsiCo loại bỏ những thứ như clorua, muối và
                những thứ khác có thể ảnh hưởng đến hương vị của nước.`,
            logo: "https://sangphatwater.com/upload/images/logo-aquafina.png"
        },
        lavie: {
            description: `Ra đời 9/1992, Lavie là công ty liên doanh giữa Perrier Vittel – Pháp(65% vốn sở hữu), thuộc tập đoàn Nestlé Waters, một công ty đứng đầu trên thế giới trong ngành nước khoáng thiên nhiên đóng chai và đối tác Việt Nam là công ty TMTH Long An`,
            logo:
                "https://www.laviewater.com/wp-content/uploads/2018/03/logo@2x.png"
        },
        dasani: {
            description: `
            Nước tinh khiết Dasani được sản xuất từ nguồn nước ngầm thông qua hệ thống thẩm thấu ngược và thanh trùng bằng Ozone, đảm bảo sự thanh khiết trong từng giọt nước giúp thanh lọc cơ thể hoàn hảo và đảm bảo an toàn cho sức khỏe.
            Vỏ chai được làm từ chất liệu thân thiện môi trường, có thể xoắn lại nhỏ gọn trong lòng bàn tay sau khi sử dụng
            Nước uống tinh khiết đóng chai Dasani là sản phẩm chất lượng của công ty Coca Cola Việt Nam.
            `,
            logo:
                "data:image/png;base64,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"
        },
        vinhHoa: {
            description: `Vĩnh Hảo là nhãn hiệu nước khoáng đầu tiên tại Việt Nam, được khai thác từ nguồn tại xã Vĩnh Hảo, huyện Tuy Phong, tỉnh Bình Thuận. Sản phẩm chính của Vĩnh Hảo là nước khoáng có ga (trước đây gọi là nước suối Vĩnh Hảo) và nước khoáng không ga, thích hợp dùng hằng ngày (nhờ có hàm lượng khoáng thấp). Ngoài ra còn có các loại nước uống giải khát (nước ngọt) được sản xuất trên nền nước khoáng này, đặc biệt là nước Khoáng Chanh (nhãn Lemona) rất được người tiêu dùng yêu thích.`,
            logo:
                "http://galaxyfoodvietnam.com.vn/timthumb.php?src=upload/product/logovinhhao-335.png&h=260&w=365&zc=2"
        }
    }
});
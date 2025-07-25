from module.Localizer.LocalizerZH import LocalizerZH

class LocalizerVI(LocalizerZH):

    # Giữ lại
    switch_language: str = (
        "请选择应用语言，新的语言设置将在下次启动时生效 …"
        "\n"
        "Select application language, changes will take effect on restart …"
        "\n"
        "Vui lòng chọn ngôn ngữ ứng dụng, cài đặt ngôn ngữ mới sẽ có hiệu lực sau khi khởi động lại …"

    )
    switch_language_toast: str = (
        "应用语言切换成功，请重启应用生效 …"
        "\n"
        "Language switched successfully, please restart the application for changes to take effect …"
        "\n"
        "Chuyển đổi ngôn ngữ thành công, vui lòng khởi động lại ứng dụng để thay đổi có hiệu lực …"
    )

    # Chung
    add: str = "Thêm"
    edit: str = "Sửa"
    none: str = "Không có"
    back: str = "Quay lại"
    next: str = "Tiếp theo"
    stop: str = "Dừng"
    start: str = "Bắt đầu"
    timer: str = "Hẹn giờ"
    close: str = "Đóng"
    alert: str = "Thông báo"
    warning: str = "Cảnh báo"
    confirm: str = "Xác nhận"
    cancel: str = "Hủy"
    auto: str = "Tự động"
    wiki: str = "Wiki"
    open: str = "Mở"
    select: str = "Chọn"
    inject: str = "Chèn"
    filter: str = "Lọc"
    search: str = "Tìm kiếm"
    generate: str = "Tạo"
    placeholder: str = "Vui lòng nhập từ khóa …"
    task_success: str = "Tác vụ đã thành công …"
    alert_no_data: str = "Không có dữ liệu hợp lệ …"
    alert_reset_timer: str = "Xác nhận đặt lại hẹn giờ?"
    alert_reset_translation: str = "Xác nhận đặt lại tác vụ dịch và bắt đầu một tác vụ mới?"

    # Trang chính
    app_close_message_box: str = "Bạn có chắc chắn muốn thoát khỏi ứng dụng không … ?"
    app_new_version: str = "Tải phiên bản mới!"
    app_new_version_toast: str = "Đã tìm thấy phiên bản mới, phiên bản: {VERSION}. Vui lòng nhấp vào nút ở góc dưới bên trái để tải xuống và cập nhật …"
    app_new_version_update: str = "Đang tải xuống {PERCENT} …"
    app_new_version_failure: str = "Tải xuống phiên bản mới thất bại …"
    app_new_version_success: str = "Tải xuống phiên bản mới thành công …"
    app_new_version_downloaded: str = "Nhấp để áp dụng phiên bản mới!"
    app_new_version_waiting_restart: str = "Cập nhật hoàn tất, ứng dụng sẽ sớm đóng lại …"
    app_theme_btn: str = "Giao diện"
    app_language_btn: str = "Ngôn ngữ"
    app_settings_page: str = "Cài đặt ứng dụng"
    app_platform_page: str = "API"
    app_project_page: str = "Cài đặt dự án"
    app_translation_page: str = "Bắt đầu dịch"
    app_basic_settings_page: str = "Cài đặt cơ bản"
    app_expert_settings_page: str = "Cài đặt chuyên gia"
    app_glossary_page: str = "Bảng thuật ngữ"
    app_text_preserve_page: str = "Bảo vệ văn bản"
    app_text_replacement_page: str = "Thay thế văn bản"
    app_pre_translation_replacement_page: str = "Thay thế trước dịch"
    app_post_translation_replacement_page: str = "Thay thế sau dịch"
    app_custom_prompt_navigation_item: str = "Prompt tùy chỉnh"
    app_custom_prompt_zh_page: str = "Prompt tiếng Trung"
    app_custom_prompt_en_page: str = "Prompt tiếng Anh"
    app_laboratory_page: str = "Phòng thí nghiệm"
    app_treasure_chest_page: str = "Hộp báu vật"

    # Đường dẫn
    path_bilingual: str = "song_ngu"
    path_glossary_export: str = "xuat_bang_thuat_ngu"
    path_text_preserve_export: str = "xuat_bao_ve_van_ban"
    path_pre_translation_replacement_export: str = "xuat_thay_the_truoc_dich"
    path_post_translation_replacement_export: str = "xuat_thay_the_sau_dich"
    path_result_check_kana: str = "ket_qua_kiem_tra_kana_con_sot.json"
    path_result_check_hangeul: str = "ket_qua_kiem_tra_hangeul_con_sot.json"
    path_result_check_text_preserve: str = "ket_qua_kiem_tra_bao_ve_van_ban.json"
    path_result_check_similarity: str = "ket_qua_kiem_tra_do_tuong_dong_cao.json"
    path_result_check_glossary: str = "ket_qua_kiem_tra_thuat_ngu_sai.json"
    path_result_check_untranslated: str = "ket_qua_kiem_tra_muc_chua_dich.json"
    path_result_check_retry_count_threshold: str = "ket_qua_kiem_tra_dat_nguong_thu_lai.json"
    path_result_batch_correction: str = "sua_loi_hang_loat.xlsx"
    path_result_name_field_extraction: str = "trich_xuat_truong_ten.xlsx"

    # Nhật ký (Log)
    log_proxy: str = "Đã bật proxy mạng …"
    log_expert_mode: str = "Đã bật Chế độ chuyên gia …"
    log_api_test_fail: str = "Kiểm tra API thất bại … "
    log_task_fail: str = "Tác vụ dịch thất bại …"
    log_read_file_fail: str = "Đọc tệp thất bại …"
    log_write_file_fail: str = "Ghi tệp thất bại …"
    log_read_cache_file_fail: str = "Không thể đọc dữ liệu cache từ tệp …"
    log_write_cache_file_fail: str = "Không thể ghi dữ liệu cache vào tệp …"
    log_crash: str = "Đã xảy ra lỗi nghiêm trọng, chương trình sẽ thoát. Chi tiết lỗi đã được lưu vào tệp nhật ký …"
    cli_verify_folder: str = "lỗi tham số: đường dẫn không hợp lệ …"
    cli_verify_language: str = "lỗi tham số: ngôn ngữ không hợp lệ …"
    translator_max_round: str = "Số vòng tối đa"
    translator_current_round: str = "Vòng hiện tại"
    translator_api_url: str = "URL API"
    translator_name: str = "Tên API"
    translator_model: str = "Tên Model"
    translator_writing: str = "Đang ghi dữ liệu dịch, vui lòng đợi …"
    translator_done: str = "Tất cả văn bản đã được dịch, tác vụ dịch hoàn tất …"
    translator_fail: str = "Đã đạt số vòng dịch tối đa, một số văn bản vẫn chưa được dịch. Vui lòng kiểm tra kết quả dịch …"
    translator_stop: str = "Tác vụ dịch đã dừng …"
    translator_write: str = "Kết quả dịch đã được lưu vào thư mục {PATH} …"
    translator_task_generation_log: str = "Tạo tác vụ hoàn tất, đã tạo tổng cộng {COUNT} tác vụ …"
    translator_rule_filter_log: str = "Lọc theo quy tắc hoàn tất, đã lọc tổng cộng {COUNT} mục không cần dịch …"
    translator_language_filter_log: str = "Lọc theo ngôn ngữ hoàn tất, đã lọc tổng cộng {COUNT} mục không chứa ngôn ngữ đích …"
    translator_mtool_optimizer_pre_log: str = "Tiền xử lý MToolOptimizer hoàn tất, đã lọc tổng cộng {COUNT} mục chứa các mệnh đề trùng lặp …"
    translator_mtool_optimizer_post_log: str = "Hậu xử lý MToolOptimizer hoàn tất …"
    translator_task_response_think: str = "Model đang suy nghĩ:\n"
    translator_task_response_result: str = "Phản hồi của Model:\n"
    translator_response_check_fail: str = "Văn bản đã dịch không qua kiểm tra, sẽ tự động thử lại trong vòng dịch tiếp theo"
    translator_response_check_fail_all: str = "Tất cả văn bản đã dịch không qua kiểm tra, sẽ tự động thử lại trong vòng dịch tiếp theo"
    translator_response_check_fail_part: str = "Một phần văn bản đã dịch không qua kiểm tra, sẽ tự động thử lại trong vòng dịch tiếp theo"
    translator_task_success: str = "Thời gian tác vụ {TIME} giây, {LINES} dòng văn bản, token đầu vào {PT}, token đầu ra {CT}"
    translator_too_many_task: str = "Quá nhiều tác vụ thời gian thực. Chi tiết bị ẩn để đảm bảo hiệu suất …"
    translator_no_items: str = "Không tìm thấy dữ liệu có thể dịch. Vui lòng kiểm tra lại tệp đầu vào và cài đặt dự án …"
    translator_running: str = "Tác vụ đang chạy, vui lòng thử lại sau …"
    file_checker_kana: str = "Kiểm tra Kana còn sót hoàn tất, không tìm thấy vấn đề …"
    file_checker_kana_full: str = "Kiểm tra Kana còn sót hoàn tất, tìm thấy {COUNT} vấn đề, {PERCENT}%, kết quả đã được ghi vào [green]{TARGET}[/] …"
    file_checker_hangeul: str = "Kiểm tra Hangeul còn sót hoàn tất, không tìm thấy vấn đề …"
    file_checker_hangeul_full: str = "Kiểm tra Hangeul còn sót hoàn tất, tìm thấy {COUNT} vấn đề, {PERCENT}%, kết quả đã được ghi vào [green]{TARGET}[/] …"
    file_checker_text_preserve: str = "Kiểm tra bảo vệ văn bản hoàn tất, không tìm thấy vấn đề …."
    file_checker_text_preserve_full: str = "Kiểm tra bảo vệ văn bản hoàn tất, tìm thấy {COUNT} vấn đề tiềm ẩn ({PERCENT}%), kết quả đã được ghi vào [green]{TARGET}[/] …."
    file_checker_text_preserve_alert_key: str = "____CẢNH_BÁO____"
    file_checker_text_preserve_alert_value: str = "Tệp này liệt kê các mục mà việc bảo vệ văn bản **có thể** đã không hoạt động chính xác. Vui lòng xác minh trong ngữ cảnh!!"
    file_checker_similarity: str = "Kiểm tra độ tương đồng hoàn tất, không tìm thấy vấn đề …"
    file_checker_similarity_full: str = "Kiểm tra độ tương đồng hoàn tất, tìm thấy {COUNT} vấn đề tiềm ẩn, {PERCENT}%, kết quả đã được ghi vào [green]{TARGET}[/] …"
    file_checker_similarity_alert_key: str = "____CẢNH_BÁO____"
    file_checker_similarity_alert_value: str = "Tệp này liệt kê các mục có độ tương đồng *có thể* cao. Vui lòng xác minh trong ngữ cảnh!"
    file_checker_glossary: str = "Kiểm tra bảng thuật ngữ hoàn tất, không tìm thấy vấn đề …"
    file_checker_glossary_full: str = "Kiểm tra bảng thuật ngữ hoàn tất, tìm thấy {COUNT} vấn đề, {PERCENT}%, kết quả đã được ghi vào [green]{TARGET}[/] …"
    platofrm_tester_key: str = "Đang kiểm tra Khóa API"
    platofrm_tester_messages: str = "Prompt tác vụ:"
    platofrm_tester_response_think: str = "Model đang suy nghĩ:"
    platofrm_tester_response_result: str = "Phản hồi của Model:"
    platofrm_tester_result: str = "Đã kiểm tra tổng cộng {COUNT} API, {SUCCESS} thành công, {FAILURE} thất bại …"
    platofrm_tester_result_failure: str = "Các khóa bị lỗi:"
    platofrm_tester_running: str = "Tác vụ đang chạy, vui lòng thử lại sau …"
    response_checker_unknown: str = "Không xác định"
    response_checker_fail_data: str = "Lỗi cấu trúc dữ liệu"
    response_checker_fail_line_count: str = "Số dòng không khớp"
    response_checker_line_error_kana: str = "Kana còn sót"
    response_checker_line_error_hangeul: str = "Hangeul còn sót"
    response_checker_line_error_fake_reply: str = "Phản hồi giả còn sót"
    response_checker_line_error_empty_line: str = "Dòng trống"
    response_checker_line_error_similarity: str = "Độ tương đồng cao"
    response_checker_line_error_degradation: str = "Chất lượng suy giảm"
    response_decoder_glossary_by_json: str = "Dữ liệu bảng thuật ngữ -> giải tuần tự, tổng cộng {COUNT} mục"
    response_decoder_glossary_by_rule: str = "Dữ liệu bảng thuật ngữ -> phân tích theo quy tắc sau khi tách, tổng cộng {COUNT} mục"
    response_decoder_translation_by_json: str = "Dữ liệu dịch -> giải tuần tự, tổng cộng {COUNT} mục"
    response_decoder_translation_by_rule: str = "Dữ liệu dịch -> phân tích theo quy tắc sau khi tách, tổng cộng {COUNT} mục"

    # Cài đặt ứng dụng
    app_settings_page_expert_title: str = "Chế độ chuyên gia"
    app_settings_page_expert_content: str = "Bật tính năng này sẽ hiển thị nhiều thông tin log hơn và cung cấp nhiều tùy chọn cài đặt nâng cao hơn (có hiệu lực sau khi khởi động lại ứng dụng)"
    app_settings_page_font_hinting_title: str = "Gợi ý phông chữ (Font Hinting)"
    app_settings_page_font_hinting_content: str = "Bật tính năng này sẽ làm cho các cạnh của phông chữ giao diện người dùng trở nên mượt mà hơn (có hiệu lực sau khi khởi động lại ứng dụng)"
    app_settings_page_scale_factor_title: str = "Hệ số tỷ lệ toàn cục"
    app_settings_page_scale_factor_content: str = "Bật tính năng này sẽ thay đổi tỷ lệ giao diện ứng dụng theo tỷ lệ đã chọn (có hiệu lực sau khi khởi động lại ứng dụng)"
    app_settings_page_proxy_url: str = "Ví dụ - http://127.0.0.1:7890"
    app_settings_page_proxy_url_title: str = "Proxy mạng"
    app_settings_page_proxy_url_content: str = "Bật tính năng này sẽ sử dụng địa chỉ proxy đã đặt để gửi yêu cầu mạng (có hiệu lực sau khi khởi động lại ứng dụng)"
    app_settings_page_close: str = "Ứng dụng sẽ đóng, vui lòng xác nhận …"

    # Quản lý giao diện (API)
    platform_page_api_test_result: str = "Kết quả kiểm tra API: {SUCCESS} thành công, {FAILURE} thất bại …"
    platform_page_api_activate: str = "Kích hoạt API"
    platform_page_api_edit: str = "Sửa API"
    platform_page_api_args: str = "Sửa tham số"
    platform_page_api_test: str = "Kiểm tra API"
    platform_page_api_delete: str = "Xóa API"
    platform_page_widget_add_title: str = "Danh sách API"
    platform_page_widget_add_content: str = "Thêm và quản lý bất kỳ API LLM nào tương thích với các định dạng của Google, OpenAI và Anthropic tại đây"

    # Sửa giao diện (API)
    platform_edit_page_name: str = "Vui lòng nhập tên API …"
    platform_edit_page_name_title: str = "Tên API"
    platform_edit_page_name_content: str = "Vui lòng nhập tên API, chỉ để hiển thị trong ứng dụng, không có tác dụng thực tế"
    platform_edit_page_api_url: str = "Vui lòng nhập URL API …"
    platform_edit_page_api_url_title: str = "URL API"
    platform_edit_page_api_url_content: str = "Vui lòng nhập URL API, chú ý xem có cần thêm /v1 ở cuối không"
    platform_edit_page_api_key: str = "Vui lòng nhập Khóa API …"
    platform_edit_page_api_key_title: str = "Khóa API"
    platform_edit_page_api_key_content: str = "Vui lòng nhập Khóa API, ví dụ: sk-d0daba12345678fd8eb7b8d31c123456. Có thể nhập nhiều khóa để sử dụng luân phiên, mỗi khóa một dòng"
    platform_edit_page_thinking_title: str = "Ưu tiên sử dụng Chế độ Suy nghĩ"
    platform_edit_page_thinking_content: str = "Đối với các model có cả chế độ suy nghĩ và chế độ thường, ưu tiên sử dụng chế độ suy nghĩ"
    platform_edit_page_model: str = "Vui lòng nhập Tên Model …"
    platform_edit_page_model_title: str = "Tên Model"
    platform_edit_page_model_content: str = "Model hiện đang sử dụng: {MODEL}"
    platform_edit_page_model_edit: str = "Nhập thủ công"
    platform_edit_page_model_sync: str = "Lấy trực tuyến"

    # Sửa tham số
    args_edit_page_top_p_title: str = "top_p"
    args_edit_page_top_p_content: str = "Vui lòng cài đặt cẩn thận, giá trị không chính xác có thể gây ra kết quả bất thường hoặc lỗi yêu cầu"
    args_edit_page_temperature_title: str = "temperature"
    args_edit_page_temperature_content: str = "Vui lòng cài đặt cẩn thận, giá trị không chính xác có thể gây ra kết quả bất thường hoặc lỗi yêu cầu"
    args_edit_page_presence_penalty_title: str = "presence_penalty"
    args_edit_page_presence_penalty_content: str = "Vui lòng cài đặt cẩn thận, giá trị không chính xác có thể gây ra kết quả bất thường hoặc lỗi yêu cầu"
    args_edit_page_frequency_penalty_title: str = "frequency_penalty"
    args_edit_page_frequency_penalty_content: str = "Vui lòng cài đặt cẩn thận, giá trị không chính xác có thể gây ra kết quả bất thường hoặc lỗi yêu cầu"
    args_edit_page_document_link: str = "Nhấp để xem tài liệu"

    # Danh sách model
    model_list_page_title: str = "Danh sách Model có sẵn"
    model_list_page_content: str = "Nhấp để chọn model sẽ sử dụng"
    model_list_page_fail: str = "Không thể lấy danh sách model, vui lòng kiểm tra cấu hình API …"

    # Cài đặt dự án
    project_page_source_language_title: str = "Ngôn ngữ nguồn"
    project_page_source_language_content: str = "Đặt ngôn ngữ của văn bản đầu vào trong dự án hiện tại"
    project_page_target_language_title: str = "Ngôn ngữ đích"
    project_page_target_language_content: str = "Đặt ngôn ngữ của văn bản đầu ra trong dự án hiện tại"
    project_page_input_folder_title: str = "Thư mục đầu vào"
    project_page_input_folder_content: str = "Thư mục đầu vào hiện tại là"
    project_page_output_folder_title: str = "Thư mục đầu ra (Không được trùng với thư mục đầu vào)"
    project_page_output_folder_content: str = "Thư mục đầu ra hiện tại là"
    project_page_output_folder_open_on_finish_title: str = "Mở thư mục đầu ra khi hoàn thành tác vụ"
    project_page_output_folder_open_on_finish_content: str = "Khi bật, thư mục đầu ra sẽ tự động mở khi tác vụ hoàn thành"
    project_page_traditional_chinese_title: str = "Xuất tiếng Trung phồn thể"
    project_page_traditional_chinese_content: str = "Khi bật, văn bản tiếng Trung sẽ được xuất dưới dạng chữ phồn thể nếu ngôn ngữ đích được đặt là tiếng Trung"

    # Bắt đầu dịch
    translation_page_status_idle: str = "Nhàn rỗi"
    translation_page_status_testing: str = "Đang kiểm tra"
    translation_page_status_translating: str = "Đang dịch"
    translation_page_status_stopping: str = "Đang dừng"
    translation_page_indeterminate_saving: str = "Đang lưu tệp cache …"
    translation_page_indeterminate_stoping: str = "Đang dừng tác vụ dịch …"
    translation_page_card_time: str = "Thời gian đã trôi qua"
    translation_page_card_remaining_time: str = "Thời gian còn lại"
    translation_page_card_line: str = "Số dòng đã dịch"
    translation_page_card_remaining_line: str = "Số dòng còn lại"
    translation_page_card_speed: str = "Tốc độ trung bình"
    translation_page_card_token: str = "Tổng số Token"
    translation_page_card_task: str = "Tác vụ thời gian thực"
    translation_page_alert_pause: str = "Các tác vụ dịch đã dừng có thể được tiếp tục bất cứ lúc nào. Xác nhận dừng tác vụ … ?"
    translation_page_continue: str = "Tiếp tục tác vụ"
    translation_page_export: str = "Xuất dữ liệu tác vụ"
    translation_page_timer: str = "Thời gian chờ trước khi khởi động trễ"

    # Cài đặt cơ bản
    basic_settings_page_max_workers_title: str = "Ngưỡng tác vụ đồng thời"
    basic_settings_page_max_workers_content: str = (
        "Số lượng tác vụ tối đa thực thi đồng thời"
        "<br>"
        "Cấu hình hợp lý có thể tăng tốc đáng kể việc hoàn thành tác vụ"
        "<br>"
        "Vui lòng tham khảo tài liệu của nền tảng API để cài đặt, 0 = Tự động"
    )
    basic_settings_page_rpm_threshold_title: str = "Ngưỡng yêu cầu mỗi phút (RPM)"
    basic_settings_page_rpm_threshold_content: str = (
        "Tổng số lượng tác vụ tối đa được thực hiện mỗi phút, tức là ngưỡng <font color='darkgoldenrod'><b>RPM</b></font>"
        "<br>"
        "Một số nền tảng có thể giới hạn tốc độ yêu cầu"
        "<br>"
        "Vui lòng tham khảo tài liệu của nền tảng API để cài đặt, 0 = không giới hạn"
    )
    basic_settings_page_token_threshold_title: str = "Ngưỡng độ dài tác vụ"
    basic_settings_page_token_threshold_content: str = "Số lượng token văn bản tối đa có trong mỗi tác vụ"
    basic_settings_page_request_timeout_title: str = "Thời gian chờ yêu cầu"
    basic_settings_page_request_timeout_content: str = (
        "Thời gian tối đa (giây) chờ phản hồi của model khi gửi yêu cầu"
        "<br>"
        "Nếu không nhận được phản hồi sau thời gian chờ, tác vụ sẽ được coi là thất bại"
    )
    basic_settings_page_max_round_title: str = "Số vòng tối đa"
    basic_settings_page_max_round_content: str = "Sau khi hoàn thành một vòng tác vụ, các tác vụ thất bại sẽ được thử lại trong một vòng mới cho đến khi tất cả hoàn thành hoặc đạt đến ngưỡng số vòng"

    # Cài đặt chuyên gia
    expert_settings_page_preceding_lines_threshold: str = "Ngưỡng dòng ngữ cảnh"
    expert_settings_page_preceding_lines_threshold_desc: str = "Số lượng dòng trước tối đa được bao gồm làm ngữ cảnh cho mỗi tác vụ dịch, mặc định bị tắt"
    expert_settings_page_preceding_disable_on_local: str = "Bật Ngữ cảnh dòng cho giao diện cục bộ"
    expert_settings_page_preceding_disable_on_local_desc: str = "Các model cục bộ hoạt động tương đối kém, vì vậy tính năng Ngữ cảnh dòng thường có tác dụng tiêu cực, mặc định bị tắt"
    expert_settings_page_clean_ruby: str = "Làm sạch văn bản Ruby"
    expert_settings_page_clean_ruby_desc: str = (
        "Loại bỏ các ký tự phiên âm ruby khỏi chú thích, chỉ giữ lại văn bản chính, mặc định được bật"
        "<br>"
        "Chú thích ruby trong văn bản thường không được model hiểu đúng, làm sạch chúng có thể cải thiện chất lượng dịch"
        "<br>"
        "Các định dạng ruby được hỗ trợ bao gồm, nhưng không giới hạn ở:"
        "<br>"
        "• (漢字/かんじ) [漢字/かんじ] |漢字[かんじ]"
        "<br>"
        "• \\r[漢字,かんじ] \\rb[漢字,かんじ] [r_かんじ][ch_漢字] [ch_漢字]"
        "<br>"
        "• [ruby text=かんじ] [ruby text = かんじ] [ruby text=\"かんじ\"] [ruby text = \"かんじ\"]"
    )
    expert_settings_page_deduplication_in_trans: str = "Loại bỏ văn bản lặp lại trong tệp dự án T++"
    expert_settings_page_deduplication_in_trans_desc: str = "Trong tệp dự án T++ (tức là tệp <font color='darkgoldenrod'><b>.trans</b></font>), có loại bỏ văn bản lặp lại hay không, mặc định được bật"
    expert_settings_page_deduplication_in_bilingual: str = "Chỉ xuất một lần nếu nguồn và đích giống nhau trong tệp song ngữ"
    expert_settings_page_deduplication_in_bilingual_desc: str = "Trong phụ đề hoặc sách điện tử, có xuất văn bản chỉ một lần nếu văn bản nguồn và đích giống hệt nhau hay không, mặc định được bật"
    expert_settings_page_write_translated_name_fields_to_file: str = "Ghi các trường tên đã dịch vào tệp đầu ra"
    expert_settings_page_write_translated_name_fields_to_file_desc: str = (
        "Trong một số <font color='darkgoldenrod'><b>GalGame</b></font>, dữ liệu trường tên được liên kết với các tệp tài nguyên như hình ảnh hoặc tệp âm thanh"
        "<br>"
        "Dịch các trường tên này có thể gây ra lỗi. Trong những trường hợp như vậy, tính năng này có thể bị tắt, mặc định được bật"
        "<br>"
        "Các định dạng được hỗ trợ:"
        "<br>"
        "• Văn bản game được xuất từ RenPy (.rpy)"
        "<br>"
        "• Văn bản game có trường tên được xuất từ VNTextPatch hoặc SExtractor (.json)"
    )
    expert_settings_page_result_checker_retry_count_threshold: str = "Kiểm tra kết quả - Đạt ngưỡng số lần thử lại"
    expert_settings_page_result_checker_retry_count_threshold_desc: str = (
        "Bao gồm danh sách các mục <font color='darkgoldenrod'><b>đã đạt đến ngưỡng thử lại</b></font> trong báo cáo kiểm tra kết quả, mặc định bị tắt"
        "<br>"
        "• Trong quá trình kiểm tra kết quả dịch, nếu một mục vẫn thất bại sau khi đạt đến ngưỡng thử lại, kết quả cuối cùng sẽ được sử dụng"
        "<br>"
        "• Tính năng này cho phép bạn xác minh riêng lẻ xem kết quả cuối cùng được lấy có thực sự chính xác hay không"
    )

    # Chất lượng - Chung
    quality_import: str = "Nhập"
    quality_import_toast: str = "Dữ liệu đã được nhập …"
    quality_export: str = "Xuất"
    quality_export_toast: str = "Dữ liệu đã được xuất ra thư mục gốc của ứng dụng …"
    quality_save: str = "Lưu"
    quality_save_toast: str = "Dữ liệu đã được lưu …"
    quality_merge_duplication: str = "Dữ liệu trùng lặp đã được hợp nhất …"
    quality_preset: str = "Cài đặt sẵn"
    quality_reset: str = "Đặt lại"
    quality_reset_toast: str = "Dữ liệu đã được đặt lại …"
    quality_reset_alert: str = "Xác nhận đặt lại về dữ liệu mặc định … ?"
    quality_select_file: str = "Chọn tệp"
    quality_select_file_type: str = "Định dạng hỗ trợ (*.json *.xlsx)"
    quality_delete_row: str = "Xóa dòng"
    quality_switch_regex: str = "Chuyển đổi Regex"

    # Bảng thuật ngữ
    glossary_page_head_title: str = "Bảng thuật ngữ"
    glossary_page_head_content: str = "Bằng cách xây dựng một bảng thuật ngữ trong prompt để hướng dẫn model dịch, có thể đạt được việc dịch thống nhất và sửa lỗi đại từ nhân xưng"
    glossary_page_table_row_01: str = "Gốc"
    glossary_page_table_row_02: str = "Dịch"
    glossary_page_table_row_03: str = "Mô tả"
    glossary_page_kg: str = "Công cụ một lần nhấp"

    # Bảo vệ văn bản
    text_preserve_page_head_title: str = "Quy tắc bảo vệ văn bản tùy chỉnh"
    text_preserve_page_head_content: str = (
        "Bảo vệ các đoạn văn bản như đoạn mã, ký tự điều khiển và ký tự kiểu không nên được dịch, ngăn chặn việc dịch sai"
        "<br>"
        "<font color='darkgoldenrod'><b>Mặc định bị tắt</b></font>, trước khi bật, vui lòng đọc kỹ mô tả tính năng trong <font color='darkgoldenrod'><b>Wiki</b></font> để đảm bảo bạn hiểu đầy đủ cách sử dụng"
        "<br>"
        "• Đã bật - Bảo vệ văn bản bằng cách khớp nó với các <font color='darkgoldenrod'><b>Quy tắc biểu thức chính quy</b></font> được đặt trên trang này"
        "<br>"
        "• Đã tắt - Tự động phát hiện định dạng văn bản và engine game, và áp dụng các quy tắc bảo vệ thông minh, hoạt động tốt cho hầu hết nội dung"
    )
    text_preserve_page_table_row_01: str = "Quy tắc"
    text_preserve_page_table_row_02: str = "Ghi chú (Chỉ để tham khảo, không có tác dụng thực tế)"

    # Thay thế trước dịch
    pre_translation_replacement_page_head_title: str = "Thay thế trước dịch"
    pre_translation_replacement_page_head_content: str = (
        "Trước khi dịch, các phần khớp của văn bản gốc sẽ được thay thế bằng văn bản được chỉ định, xử lý theo thứ tự từ trên xuống dưới"
        "<br>"
        "Đối với game engine <font color='darkgoldenrod'><b>RPGMaker MV/MZ</b></font>:"
        "<br>"
        "• Nhập tệp <font color='darkgoldenrod'><b>actors.json</b></font> từ thư mục <font color='darkgoldenrod'><b>data</b></font> hoặc <font color='darkgoldenrod'><b>www\\data</b></font> trong thư mục game có thể cải thiện chất lượng dịch"
        "<br>"
        "• Cần xử lý đặc biệt cho các game có tên tùy chỉnh. Nhấp vào nút dưới cùng bên phải để xem hướng dẫn trên <font color='darkgoldenrod'><b>Wiki</b></font>"
    )
    pre_translation_replacement_page_table_row_01: str = "Gốc"
    pre_translation_replacement_page_table_row_02: str = "Thay thế"
    pre_translation_replacement_page_table_row_03: str = "Regex"

    # Thay thế sau dịch
    post_translation_replacement_page_head_title: str = "Thay thế sau dịch"
    post_translation_replacement_page_head_content: str = "Sau khi dịch xong, thay thế các phần khớp trong văn bản đã dịch bằng văn bản được chỉ định, thứ tự thực hiện từ trên xuống dưới"
    post_translation_replacement_page_table_row_01: str = "Gốc"
    post_translation_replacement_page_table_row_02: str = "Thay thế"
    post_translation_replacement_page_table_row_03: str = "Regex"

    # Prompt tùy chỉnh - Tiếng Trung
    custom_prompt_zh_page_head: str = "Prompt tiếng Trung tùy chỉnh (model SakuraLLM không hỗ trợ)"
    custom_prompt_zh_page_head_desc: str = (
        "Thêm các yêu cầu dịch bổ sung như bối cảnh câu chuyện và văn phong qua các prompt tùy chỉnh"
        "<br>"
        "Lưu ý: Tiền tố và hậu tố là cố định và không thể sửa đổi"
        "<br>"
        "Các prompt tùy chỉnh trên trang này sẽ chỉ được sử dụng khi <font color='darkgoldenrod'><b>ngôn ngữ dịch được đặt là tiếng Trung</b></font>"
    )

    # Prompt tùy chỉnh - Tiếng Anh
    custom_prompt_en_page_head: str = "Prompt tiếng Anh tùy chỉnh (model SakuraLLM không hỗ trợ)"
    custom_prompt_en_page_head_desc: str = (
        "Thêm các yêu cầu dịch bổ sung như bối cảnh câu chuyện và văn phong qua các prompt tùy chỉnh"
        "<br>"
        "Lưu ý: Tiền tố và hậu tố là cố định và không thể sửa đổi"
        "<br>"
        "Các prompt tùy chỉnh trên trang này sẽ chỉ được sử dụng khi <font color='darkgoldenrod'><b>ngôn ngữ dịch không phải là tiếng Trung</b></font>"
    )

    # Phòng thí nghiệm
    laboratory_page_mtool_optimizer_enable: str = "Trình tối ưu hóa MTool"
    laboratory_page_mtool_optimizer_enable_desc: str = (
        "Có thể giảm thời gian dịch và lượng token sử dụng lên đến 40% khi dịch văn bản MTool"
        "<br>"
        "Có thể dẫn đến các vấn đề như <font color='darkgoldenrod'><b>văn bản gốc còn sót lại</b></font> hoặc <font color='darkgoldenrod'><b>câu văn không mạch lạc</b></font>"
        "<br>"
        "Nó <font color='darkgoldenrod'><b>chỉ nên được bật khi dịch văn bản MTool</b></font>"
        "<br>"
        "Vui lòng <font color='darkgoldenrod'><b>tự quyết định</b></font> có bật tính năng này hay không"
        ""
        ""
    )
    laboratory_page_auto_glossary_enable: str = "Tự động hoàn thành bảng thuật ngữ (Không hỗ trợ SakuraLLM)"
    laboratory_page_auto_glossary_enable_desc: str = (
        "Cố gắng tự động thêm các mục danh từ riêng còn thiếu vào bảng thuật ngữ trong quá trình dịch"
        "<br>"
        "Điều này chỉ có hiệu quả khi <font color='darkgoldenrod'><b>tính năng Bảng thuật ngữ được bật</b></font>"
        "<br>"
        "Được thiết kế để bổ sung, không thay thế, <font color='darkgoldenrod'><b>KeywordGacha</b></font>, các thuật ngữ thu được sẽ được <font color='darkgoldenrod'><b>ghi trực tiếp vào bảng thuật ngữ</b></font>"
        "<br>"
        "Có thể tạo ra các <font color='darkgoldenrod'><b>mục thuật ngữ sai hoặc không phù hợp</b></font>, vui lòng <font color='darkgoldenrod'><b>tự phán đoán</b></font> xem có nên bật tính năng này hay không"
        "<br>"
        "Khuyến nghị chỉ sử dụng tính năng này với các model mạnh như DeepSeek V3/R1"
    )

    # Hộp báu vật
    tool_box_page_batch_correction: str = "Sửa lỗi hàng loạt"
    tool_box_page_batch_correction_desc: str = "Kiểm tra tệp đã dịch với kết quả dịch đã tạo và thực hiện sửa lỗi hàng loạt đối với các lỗi tiềm ẩn, cho phép tinh chỉnh nhanh kết quả dịch"
    tool_box_page_re_translation: str = "Dịch lại một phần"
    tool_box_page_re_translation_desc: str = "Dịch lại các phần của văn bản đã được dịch dựa trên các bộ lọc đã đặt, chủ yếu để cập nhật nội dung hoặc sửa lỗi"
    tool_box_page_name_field_extraction: str = "Trích xuất trường tên"
    tool_box_page_name_field_extraction_desc: str = (
        "Trích xuất dữ liệu trường tên nhân vật từ văn bản game <font color='darkgoldenrod'><b>RenPy</b></font> và <font color='darkgoldenrod'><b>GalGame</b></font>, "
        "và tự động tạo dữ liệu bảng thuật ngữ tương ứng để tạo điều kiện cho việc dịch sau này"
    )

    # Hộp báu vật - Sửa lỗi hàng loạt
    batch_correction_page: str = "Sửa lỗi hàng loạt"
    batch_correction_page_desc: str = (
        "Kiểm tra dữ liệu trong các tệp từ kết quả dịch để sửa lỗi hàng loạt các lỗi tiềm ẩn, sau đó tạo ra các tệp dịch đã được sửa"
        "<br>"
        "Quy trình làm việc:"
        "<br>"
        "• Trích xuất dữ liệu có thể cần sửa từ tệp kiểm tra kết quả dịch trong <font color='darkgoldenrod'><b>thư mục đầu vào</b></font>"
        "<br>"
        "• Kiểm tra dữ liệu đã trích xuất và sửa các mục cần sửa theo tình hình thực tế"
        "<br>"
        "• Chèn dữ liệu đã sửa vào các tệp đã dịch trong <font color='darkgoldenrod'><b>thư mục đầu vào</b></font>, sau đó tạo các tệp dịch đã sửa trong <font color='darkgoldenrod'><b>thư mục đầu ra</b></font>"
    )
    batch_correction_page_step_01: str = "Bước 1 - Tạo dữ liệu sửa lỗi"
    batch_correction_page_step_01_desc: str = (
        "Trích xuất dữ liệu có thể chứa lỗi dịch từ tệp kiểm tra kết quả"
        "<br>"
        f"Sau đó tự động tạo một tệp dữ liệu để chỉnh sửa có tên <font color='darkgoldenrod'><b>{path_result_batch_correction}</b></font> trong <font color='darkgoldenrod'><b>Thư mục đầu ra</b></font>"
    )
    batch_correction_page_step_02: str = "Bước 2 - Chèn dữ liệu sửa lỗi"
    batch_correction_page_step_02_desc: str = (
        "Kiểm tra nội dung trong tệp dữ liệu, và sau khi xác nhận mọi thứ đều chính xác, hãy <font color='darkgoldenrod'><b>đóng</b></font> tệp để bắt đầu chèn"
        "<br>"
        "Xin lưu ý:"
        "<br>"
        "• Ngoại trừ <font color='darkgoldenrod'><b>cột sửa lỗi</b></font>, không sửa đổi dữ liệu khác trong tệp dữ liệu"
        "<br>"
        "• Tên tệp của một số định dạng có thể chứa hậu tố ngôn ngữ như <font color='darkgoldenrod'><b>.zh</b></font>, hãy xóa nó trước khi chèn để khớp dữ liệu chính xác"
    )
    batch_correction_page_title_01: str = "Tên tệp"
    batch_correction_page_title_02: str = "Loại lỗi"
    batch_correction_page_title_03: str = "Văn bản gốc (Không sửa đổi cột này)"
    batch_correction_page_title_04: str = "Văn bản đã dịch (Không sửa đổi cột này)"
    batch_correction_page_title_05: str = "Sửa lỗi (Vui lòng sửa đổi cột này)"

    # Hộp báu vật - Dịch lại một phần
    re_translation_page: str = "Dịch lại một phần"
    re_translation_page_desc: str = (
        "Sẽ lọc văn bản trong <font color='darkgoldenrod'><b>Thư mục đầu vào</b></font> dựa trên các điều kiện lọc đã đặt, sau đó dịch lại văn bản đáp ứng các điều kiện đó"
        "<br>"
        "Quy trình làm việc:"
        "<br>"
        "• Tải văn bản gốc và văn bản đã dịch từ các thư mục con <font color='darkgoldenrod'><b>src</b></font> và <font color='darkgoldenrod'><b>dst</b></font> của <font color='darkgoldenrod'><b>Thư mục đầu vào</b></font>"
        "<br>"
        "• Tên tệp và nội dung tệp của các tệp gốc và đã dịch phải tương ứng chặt chẽ một-một"
        "<br>"
        "• Lọc ra văn bản cần dịch lại theo cài đặt trên trang này, dịch nó theo quy trình bình thường"
    )
    re_translation_page_white_list: str = "Từ khóa - Danh sách trắng"
    re_translation_page_white_list_desc: str = (
        "Văn bản chứa các từ khóa này sẽ được dịch lại. Bạn có thể nhập nhiều từ khóa, mỗi từ khóa một dòng"
        "\n"
        "Chỉ cần khớp với một trong số chúng là đủ để xác định văn bản cần được dịch lại"
    )
    re_translation_page_alert_not_equal: str = "Số dòng trong văn bản gốc và văn bản đã dịch không khớp …"

    # Hộp báu vật - Trích xuất trường tên
    name_field_extraction_page: str = "Trích xuất trường tên"
    name_field_extraction_page_desc: str = (
        "Trích xuất các trường tên nhân vật từ tất cả các tệp đủ điều kiện trong <font color='darkgoldenrod'><b>thư mục đầu vào</b></font> và tự động tạo dữ liệu bảng thuật ngữ tương ứng"
        "<br>"
        "Xin lưu ý: Chức năng này <font color='darkgoldenrod'><b>không thể trích xuất thuật ngữ từ văn bản chính</b></font>, và không thể thay thế công cụ <font color='darkgoldenrod'><b>KeywordGacha</b></font>"
        "<br>"
        "Các định dạng được hỗ trợ:"
        "<br>"
        "• Văn bản game được xuất từ RenPy (.rpy)"
        "<br>"
        "• Văn bản game có trường tên được xuất từ VNTextPatch hoặc SExtractor (.json)"
    )
    name_field_extraction_page_step_01: str = "Bước 1 - Trích xuất dữ liệu"
    name_field_extraction_page_step_01_desc: str = (
        "Trích xuất các trường tên và ngữ cảnh liên quan của chúng, và gửi chúng đến trình dịch để dịch"
        "<br>"
        f"Sau khi dịch xong, tệp <font color='darkgoldenrod'><b>{path_result_name_field_extraction}</b></font> sẽ được tạo trong <font color='darkgoldenrod'><b>Thư mục đầu ra</b></font>"
    )
    name_field_extraction_page_step_02: str = "Bước 2 - Tạo bảng thuật ngữ"
    name_field_extraction_page_step_02_desc: str = (
        f"Trích xuất dữ liệu đã dịch từ tệp <font color='darkgoldenrod'><b>{path_result_name_field_extraction}</b></font> trong <font color='darkgoldenrod'><b>Thư mục đầu ra</b></font>"
        "<br>"
        "Sau đó tạo dữ liệu bảng thuật ngữ tương ứng, kiểm tra xem dữ liệu bảng thuật ngữ được tạo có chính xác hay không"
    )
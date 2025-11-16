#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to expand i18n JSON files with all missing translations
"""
import json
import os

def expand_vi_json():
    """Expand Vietnamese JSON with all missing content"""
    vi_file = 'locales/vi.json'
    
    with open(vi_file, 'r', encoding='utf-8') as f:
        vi_data = json.load(f)
    
    # Expand policies with delivery and return
    if 'delivery' not in vi_data['policies']:
        vi_data['policies']['delivery'] = {
            'title': '🚚 Chính Sách Giao Hàng',
            'timeTitle': 'Thời Gian Giao Hàng',
            'timeDesc': 'Thời gian giao hàng phụ thuộc vào số lượng và loại sản phẩm:',
            'timeItems': [
                'Dưới 100 sản phẩm: 7-10 ngày làm việc',
                '100-500 sản phẩm: 10-15 ngày làm việc',
                '500-1.000 sản phẩm: 15-20 ngày làm việc',
                'Trên 1.000 sản phẩm: 20-30 ngày làm việc (theo thỏa thuận)'
            ],
            'timeNote': 'Lưu ý: Thời gian trên được tính sau khi khách hàng đã duyệt mẫu và thanh toán tiền đặt cọc (30-50% giá trị hợp đồng).',
            'methodTitle': 'Phương Thức Giao Hàng',
            'methodItems': [
                'Giao hàng tận nơi: Miễn phí giao hàng trong nội thành Hà Nội',
                'Giao hàng tỉnh: Khách hàng chịu phí vận chuyển theo đơn vị vận chuyển (Viettel Post, J&T, Viet Nam Post...)',
                'Nhận hàng tại xưởng: Khách hàng có thể đến trực tiếp xưởng để nhận hàng, không mất phí'
            ],
            'processTitle': 'Quy Trình Giao Hàng',
            'processItems': [
                {'step': 'Thông báo', 'desc': 'Chúng tôi sẽ thông báo trước 1-2 ngày khi sản phẩm sẵn sàng giao hàng'},
                {'step': 'Xác nhận', 'desc': 'Xác nhận lại địa chỉ giao hàng và thời gian với khách hàng'},
                {'step': 'Giao hàng', 'desc': 'Giao hàng theo đúng địa chỉ và thời gian đã hẹn'},
                {'step': 'Nghiệm thu', 'desc': 'Khách hàng kiểm tra số lượng, chất lượng và ký nghiệm thu'},
                {'step': 'Thanh toán', 'desc': 'Thanh toán phần còn lại (nếu còn)'}
            ],
            'commitmentTitle': 'Cam Kết Giao Hàng',
            'commitmentItems': [
                'Giao hàng đúng số lượng theo hợp đồng',
                'Giao hàng đúng thời gian đã cam kết',
                'Đóng gói cẩn thận, đảm bảo sản phẩm không bị hư hỏng trong quá trình vận chuyển',
                'Mỗi sản phẩm được đóng gói riêng, có nhãn ghi size, tên người nhận (nếu có)'
            ],
            'lateTitle': 'Xử Lý Khi Giao Hàng Muộn',
            'lateDesc': 'Nếu chúng tôi giao hàng muộn so với thời gian cam kết (trừ trường hợp bất khả kháng):',
            'lateItems': [
                'Chúng tôi sẽ thông báo và xin lỗi khách hàng',
                'Giảm 5-10% giá trị đơn hàng (tùy theo mức độ muộn)',
                'Ưu tiên xử lý đơn hàng của khách hàng'
            ]
        }
    
    if 'return' not in vi_data['policies']:
        vi_data['policies']['return'] = {
            'title': '🔄 Chính Sách Đổi Trả',
            'conditionsTitle': 'Điều Kiện Đổi Trả',
            'conditionsDesc': 'Khách hàng có quyền đổi trả sản phẩm trong các trường hợp sau:',
            'conditionsItems': [
                'Sai size: Size không đúng với thông tin đã đặt (nếu do lỗi của chúng tôi)',
                'Sai mẫu: Sản phẩm không đúng với mẫu đã được duyệt',
                'Sai màu: Màu sắc không đúng với yêu cầu',
                'Lỗi sản xuất: Sản phẩm có lỗi từ nhà sản xuất (thuộc phạm vi bảo hành)',
                'Sai số lượng: Thiếu hoặc thừa số lượng so với đơn hàng'
            ],
            'timeTitle': 'Thời Gian Đổi Trả',
            'timeItems': {
                'size': 'Đổi size: Trong vòng 7 ngày kể từ ngày nhận hàng',
                'color': 'Đổi màu/mẫu: Trong vòng 3 ngày kể từ ngày nhận hàng',
                'defect': 'Đổi do lỗi: Trong thời hạn bảo hành (xem chính sách bảo hành)'
            },
            'productConditionsTitle': 'Điều Kiện Sản Phẩm Đổi Trả',
            'productConditionsDesc': 'Sản phẩm đổi trả phải đáp ứng các điều kiện sau:',
            'productConditionsItems': [
                'Còn nguyên vẹn, chưa qua sử dụng',
                'Còn đầy đủ phụ kiện, nhãn mác',
                'Chưa giặt, chưa ủi',
                'Không có vết bẩn, mùi lạ',
                'Còn hóa đơn/phiếu giao hàng'
            ],
            'processTitle': 'Quy Trình Đổi Trả',
            'processItems': [
                {'step': 'Liên hệ', 'desc': 'Khách hàng liên hệ với chúng tôi qua điện thoại hoặc email để thông báo về yêu cầu đổi trả'},
                {'step': 'Xác nhận', 'desc': 'Chúng tôi xác nhận lý do đổi trả và kiểm tra điều kiện'},
                {'step': 'Vận chuyển', 'desc': 'Khách hàng gửi lại sản phẩm về địa chỉ của chúng tôi. Chúng tôi chịu phí vận chuyển nếu do lỗi của chúng tôi. Khách hàng chịu phí vận chuyển nếu do yêu cầu đổi size/màu (trong 7 ngày đầu)'},
                {'step': 'Xử lý', 'desc': 'Chúng tôi kiểm tra và xử lý đổi trả trong vòng 3-5 ngày'},
                {'step': 'Giao hàng', 'desc': 'Giao lại sản phẩm đã đổi cho khách hàng'}
            ],
            'notesTitle': 'Lưu Ý',
            'notes': [
                'Mỗi sản phẩm chỉ được đổi trả 1 lần (trừ trường hợp lỗi từ nhà sản xuất)',
                'Nếu khách hàng yêu cầu đổi sang mẫu khác có giá cao hơn, cần thanh toán thêm phần chênh lệch',
                'Nếu khách hàng yêu cầu đổi sang mẫu khác có giá thấp hơn, chúng tôi sẽ hoàn lại phần chênh lệch',
                'Việc đổi trả do lỗi của chúng tôi sẽ được xử lý miễn phí hoàn toàn'
            ]
        }
    
    vi_data['policies']['ctaTitle'] = 'Bạn Có Câu Hỏi Về Chính Sách?'
    vi_data['policies']['ctaDesc'] = 'Liên hệ với chúng tôi để được giải đáp thắc mắc'
    vi_data['policies']['ctaContact'] = 'Liên hệ ngay'
    vi_data['policies']['ctaCall'] = 'Gọi: 0366 333 168'
    
    # Save
    with open(vi_file, 'w', encoding='utf-8') as f:
        json.dump(vi_data, f, ensure_ascii=False, indent=2)
    
    print('✅ Đã mở rộng policies (delivery, return) trong vi.json')

if __name__ == '__main__':
    expand_vi_json()


from gmail import GMail, Message

def send_msg(accepted, service_name, user_email):
    gmail = GMail('honganhc4e16@gmail.com','c4e162018')
    if accepted:
        template ="Yêu cầu của bạn đã với đối tượng {{service_name}} được phê duyệt, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của 'Mùa Đông Không Lạnh'"
    else:
        template = "Yêu cầu của bạn với đối tượng {{service_name}} đã bị từ chối. Để biết thêm chi tiết vui lòng liên hệ với người quản lý. Cảm ơn bạn đã sử dụng dịch vụ của 'Mùa Đông Không Lạnh'"

    content = template.replace('{{service_name}}', service_name)
    msg = Message("Thông báo xử lý yêu cầu",to=user_email,text=content)
    gmail.send(msg)

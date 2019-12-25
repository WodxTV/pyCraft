from minecraft.networking.connection import Connection
from minecraft.networking.packets import clientbound, serverbound

def join_game_event(packet):
    print('[*] Connected')
    chat_packet = serverbound.play.ChatPacket()
    chat_packet.message = 'I am not a bot'
    bot.write_packet(chat_packet)

if __name__ == '__main__':
    bot = Connection(address='127.0.0.1', port=25565, username='pyCraft', spoof_uuid='069a79f444e94726a5befca90e38aaf5', spoof_ip='255.255.255.255')
    bot.register_packet_listener(join_game_event, clientbound.play.JoinGamePacket)
    bot.connect()
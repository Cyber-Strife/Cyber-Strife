# nft_manager.py

class NFTManager:
    def __init__(self):
        self.nfts = {}

    def create_nft(self, nft_id, nft_details):
        self.nfts[nft_id] = nft_details
        return f"NFT {nft_id} created successfully!"

    def transfer_nft(self, nft_id, to_address):
        if nft_id in self.nfts:
            nft = self.nfts.pop(nft_id)
            return f"NFT {nft_id} transferred to {to_address}."
        else:
            return "NFT not found."

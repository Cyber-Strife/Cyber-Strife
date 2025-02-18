// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract Marketplace {
    struct Item {
        uint256 tokenId;
        address owner;
        uint256 price;
        bool isForSale;
    }

    mapping(uint256 => Item) public items;
    mapping(address => uint256[]) public ownerItems;

    function listItem(uint256 tokenId, uint256 price) public {
        items[tokenId] = Item({
            tokenId: tokenId,
            owner: msg.sender,
            price: price,
            isForSale: true
        });

        ownerItems[msg.sender].push(tokenId);
    }

    function buyItem(uint256 tokenId) public payable {
        Item storage item = items[tokenId];
        
        require(item.isForSale, "Item is not for sale");
        require(msg.value == item.price, "Incorrect price");

        payable(item.owner).transfer(msg.value);
        item.owner = msg.sender;
        item.isForSale = false;

        ownerItems[msg.sender].push(tokenId);
    }
}

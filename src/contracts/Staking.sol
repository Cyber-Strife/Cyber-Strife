// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Staking {
    ERC20 public token;
    mapping(address => uint256) public stakedAmount;

    constructor(ERC20 _token) {
        token = _token;
    }

    function stake(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        stakedAmount[msg.sender] += amount;
        token.transferFrom(msg.sender, address(this), amount);
    }

    function unstake(uint256 amount) public {
        require(stakedAmount[msg.sender] >= amount, "Insufficient balance");
        stakedAmount[msg.sender] -= amount;
        token.transfer(msg.sender, amount);
    }
}

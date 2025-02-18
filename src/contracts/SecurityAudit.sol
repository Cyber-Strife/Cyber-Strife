// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecurityAudit {
    mapping(address => uint256) public contractAuditScores;

    function auditContract(address contractAddress, uint256 score) public {
        contractAuditScores[contractAddress] = score;
    }

    function getAuditScore(address contractAddress) public view returns (uint256) {
        return contractAuditScores[contractAddress];
    }
}
